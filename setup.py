# This file is part of actmon.

# actmon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# actmon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with actmon.  If not, see <http://www.gnu.org/licenses/>.


from distutils.core import setup, Extension


module = Extension('actmon',
                   define_macros = [('MAJOR_VERSION', '0'),
                                    ('MINOR_VERSION', '1')],
                   include_dirs = ['/usr/include'],
                   libraries = ['X11', 'Xext', 'Xss'],
                   library_dirs = ['/usr/lib'],
                   sources = ['actmon.c'])


# patch distutils if it can't cope with the "classifiers" or
# "download_url" keywords
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

setup(name = 'actmon',
      version = '0.1',
      author = 'Alexandre Gravier',
      author_email = 'al.gravier@gmail.com',
      url = 'http://github.com/agravier/actmon',
      description = 'This package provides a user idle timer for X11.',
      long_description = 'This package provides a user idle timer for X11.',
      license = 'GNU General Public License (GPL) v3 and later',
      platforms = ['X11'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: No Input/Output (Daemon)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: C',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration',
        'Topic :: System :: Monitoring'],
      ext_modules = [module])
