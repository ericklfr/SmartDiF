# Install script for directory: /Users/tiagojc/Documents/github/IBTSFIF/illuminants

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/core/common/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/core/storage/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/reflectance/rbase/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/modules/color_processing/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/modules/superpixels/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/modules/computational_geometry/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/reflectance/illumestimators/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/reflectance/iic_commands/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/reflectance/iic_misc/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/reflectance/iic_estimator/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/reflectance/iic_eval/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/reflectance/iic_mask/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/reflectance/lille/cmake_install.cmake")
  include("/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/core/shell/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/Users/tiagojc/Documents/github/IBTSFIF/illuminants/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
