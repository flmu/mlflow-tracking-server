from __future__ import unicode_literals

import sys
import os
import logging
from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.nose_exclude')

if sys.version_info > (3,):
    get_method_class = lambda x: x.__self__.__class__
else:
    get_method_class = lambda x: x.im_class


class NoseExclude(Plugin):

    def options(self, parser, env=os.environ):
        """Define the command line options for the plugin."""
        super(NoseExclude, self).options(parser, env)
        env_dirs = []
        env_tests = []

        if 'NOSE_EXCLUDE_DIRS' in env:
            exclude_dirs = env.get('NOSE_EXCLUDE_DIRS', '')
            env_dirs.extend(exclude_dirs.split(';'))

        if 'NOSE_EXCLUDE_TESTS' in env:
            exclude_tests = env.get('NOSE_EXCLUDE_TESTS', '')
            env_tests.extend(exclude_tests.split(';'))

        parser.add_option(
            str("--exclude-dir"), action="append",
            dest="exclude_dirs",
            default=env_dirs,
            help="Directory to exclude from test discovery. \
                Path can be relative to current working directory \
                or an absolute path. May be specified multiple \
                times. [NOSE_EXCLUDE_DIRS]")

        parser.add_option(
            str("--exclude-dir-file"), type="string",
            dest="exclude_dir_file",
            default=env.get('NOSE_EXCLUDE_DIRS_FILE', False),
            help="A file containing a list of directories to exclude \
                from test discovery. Paths can be relative to current \
                working directory or an absolute path. \
                [NOSE_EXCLUDE_DIRS_FILE]")

        parser.add_option(
            str("--exclude-test"), action="append",
            dest="exclude_tests",
            default=env_tests,
            help="Fully qualified name of test method or class to exclude \
            from test discovery.")

        parser.add_option(
            str("--exclude-test-file"), type="string",
            dest="exclude_test_file",
            default=False,
            help="A file containing a list of fully qualified names of \
                test methods or classes to exclude from test discovery.")

    def _force_to_abspath(self, pathname, root):
        if os.path.isabs(pathname):
            abspath = pathname
        else:
            abspath = os.path.abspath(os.path.join(root, pathname))

        if os.path.exists(abspath):
            return abspath
        else:
            log.warning('The following path was not found: %s' % pathname)

    def _load_from_file(self, filename):
        with open(filename, 'r') as infile:
            new_list = [l.strip() for l in infile.readlines() if l.strip()
                        and not l.startswith('#')]
        return new_list

    def configure(self, options, conf):
        """Configure plugin based on command line options"""
        super(NoseExclude, self).configure(options, conf)

        self.exclude_dirs = {}
        self.exclude_tests = options.exclude_tests[:]

        # preload directories from file
        if options.exclude_dir_file:
            if not options.exclude_dirs:
                options.exclude_dirs = []

            new_dirs = self._load_from_file(options.exclude_dir_file)
            options.exclude_dirs.extend(new_dirs)

        if options.exclude_test_file:
            exc_tests = self._load_from_file(options.exclude_test_file)
            self.exclude_tests.extend(exc_tests)

        if not options.exclude_dirs and not self.exclude_tests:
            self.enabled = False
            return

        self.enabled = True
        if conf and conf.workingDir:
            # Use nose's working directory
            root = conf.workingDir
        else:
            root = os.getcwd()

        log.debug('cwd: %s' % root)

        # Normalize excluded directory names for lookup
        for exclude_param in options.exclude_dirs:
            # when using setup.cfg, you can specify only one 'exclude-dir'
            # separated by some character (new line is good enough)
            for d in exclude_param.split('\n'):
                d = d.strip()
                abs_d = self._force_to_abspath(d, root)
                if abs_d:
                    self.exclude_dirs[abs_d] = True

        exclude_str = "excluding dirs: %s" % ",".join(list(self.exclude_dirs.keys()))
        log.debug(exclude_str)

    def wantDirectory(self, dirname):
        """Check if directory is eligible for test discovery"""
        # In case of symbolic paths
        dirname = os.path.realpath(dirname)

        if dirname in self.exclude_dirs:
            log.debug("excluded: %s" % dirname)
            return False
        else:
            return None

    def wantModule(self, module):
        """Filter out tests based on: <module path>.<module name>"""
        if module.__name__ in self.exclude_tests:
            return False
        else:
            return None

    def wantFunction(self, fun):
        """Filter out tests based on: <module path>.<func name>"""
        fqn = '%s.%s' % (fun.__module__, fun.__name__)
        if fqn in self.exclude_tests:
            return False
        else:
            return None

    def wantMethod(self, meth):
        """Filter out tests based on <module path>.<class>.<method name>"""
        try:
            cls = get_method_class(meth)
        except AttributeError:
            return None

        fqn = '%s.%s.%s' % (cls.__module__, cls.__name__, meth.__name__)
        if fqn in self.exclude_tests:
            return False
        else:
            return None

    def wantClass(self, cls):
        """Filter out the class based on <module path>.<class name>"""
        fqn = '%s.%s' % (cls.__module__, cls.__name__)
        if fqn in self.exclude_tests:
            return False
        else:
            return None
