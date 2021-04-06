from distutils.core import setup
from Cython.Build import cythonize
fileSet = set()
fileSet.add("motion/views.py")
fileSet.add("motion/views3.py")
fileSet.add("motion/viewso.py")
fileSet.add("motion/urls.py")
fileSet.add("motion/camerasync.py")
fileSet.add("motion/admin.py")
fileSet.add("motion/apps.py")
fileSet.add("motion/models.py")
fileSet.add("motion/tests.py")
fileSet.add("motion/store_api.py")
setup(
   ext_modules=cythonize(fileSet)
)

#USAGE :  python compile.py build_ext --inplace