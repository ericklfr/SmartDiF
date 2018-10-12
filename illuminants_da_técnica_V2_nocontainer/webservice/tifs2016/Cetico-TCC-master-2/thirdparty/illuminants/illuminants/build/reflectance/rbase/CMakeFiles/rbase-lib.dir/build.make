# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/fausto/IBTSFIF-master/illuminants

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/fausto/IBTSFIF-master/illuminants/build

# Include any dependencies generated for this target.
include reflectance/rbase/CMakeFiles/rbase-lib.dir/depend.make

# Include the progress variables for this target.
include reflectance/rbase/CMakeFiles/rbase-lib.dir/progress.make

# Include the compile flags for this target's objects.
include reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make

reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o: ../rbase/shi_db_entry.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/shi_db_entry.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/shi_db_entry.cpp > CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/shi_db_entry.cpp -o CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o


reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o: ../rbase/db_index_shi.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/db_index_shi.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/db_index_shi.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/db_index_shi.cpp > CMakeFiles/rbase-lib.dir/db_index_shi.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/db_index_shi.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/db_index_shi.cpp -o CMakeFiles/rbase-lib.dir/db_index_shi.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o


reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o: ../rbase/db_index_shida.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/db_index_shida.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/db_index_shida.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/db_index_shida.cpp > CMakeFiles/rbase-lib.dir/db_index_shida.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/db_index_shida.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/db_index_shida.cpp -o CMakeFiles/rbase-lib.dir/db_index_shida.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o


reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o: ../rbase/db_descriptor.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/db_descriptor.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/db_descriptor.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/db_descriptor.cpp > CMakeFiles/rbase-lib.dir/db_descriptor.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/db_descriptor.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/db_descriptor.cpp -o CMakeFiles/rbase-lib.dir/db_descriptor.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o


reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o: ../rbase/img_read.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/img_read.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/img_read.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/img_read.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/img_read.cpp > CMakeFiles/rbase-lib.dir/img_read.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/img_read.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/img_read.cpp -o CMakeFiles/rbase-lib.dir/img_read.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o


reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o: ../rbase/img_read_config.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/img_read_config.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/img_read_config.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/img_read_config.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/img_read_config.cpp > CMakeFiles/rbase-lib.dir/img_read_config.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/img_read_config.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/img_read_config.cpp -o CMakeFiles/rbase-lib.dir/img_read_config.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o


reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o: ../rbase/color_space.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/color_space.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/color_space.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/color_space.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/color_space.cpp > CMakeFiles/rbase-lib.dir/color_space.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/color_space.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/color_space.cpp -o CMakeFiles/rbase-lib.dir/color_space.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o


reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o: ../rbase/mask.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_8) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/mask.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/mask.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/mask.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/mask.cpp > CMakeFiles/rbase-lib.dir/mask.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/mask.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/mask.cpp -o CMakeFiles/rbase-lib.dir/mask.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o


reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o: ../rbase/illum.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_9) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/illum.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/illum.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/illum.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/illum.cpp > CMakeFiles/rbase-lib.dir/illum.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/illum.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/illum.cpp -o CMakeFiles/rbase-lib.dir/illum.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o


reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o: ../rbase/color.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_10) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/color.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/color.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/color.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/color.cpp > CMakeFiles/rbase-lib.dir/color.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/color.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/color.cpp -o CMakeFiles/rbase-lib.dir/color.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o


reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o: ../rbase/commands/command_srgb2rgb.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_11) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/commands/command_srgb2rgb.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/commands/command_srgb2rgb.cpp > CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/commands/command_srgb2rgb.cpp -o CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o


reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o: reflectance/rbase/CMakeFiles/rbase-lib.dir/flags.make
reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o: ../rbase/srgb2rgb_config.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_12) "Building CXX object reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o -c /home/fausto/IBTSFIF-master/illuminants/rbase/srgb2rgb_config.cpp

reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.i"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/fausto/IBTSFIF-master/illuminants/rbase/srgb2rgb_config.cpp > CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.i

reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.s"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/fausto/IBTSFIF-master/illuminants/rbase/srgb2rgb_config.cpp -o CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.s

reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o.requires:

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o.requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o.provides: reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o.requires
	$(MAKE) -f reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o.provides.build
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o.provides

reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o.provides.build: reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o


# Object files for target rbase-lib
rbase__lib_OBJECTS = \
"CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o" \
"CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o" \
"CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o" \
"CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o" \
"CMakeFiles/rbase-lib.dir/img_read.cpp.o" \
"CMakeFiles/rbase-lib.dir/img_read_config.cpp.o" \
"CMakeFiles/rbase-lib.dir/color_space.cpp.o" \
"CMakeFiles/rbase-lib.dir/mask.cpp.o" \
"CMakeFiles/rbase-lib.dir/illum.cpp.o" \
"CMakeFiles/rbase-lib.dir/color.cpp.o" \
"CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o" \
"CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o"

# External object files for target rbase-lib
rbase__lib_EXTERNAL_OBJECTS =

reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/build.make
reflectance/rbase/librbase-lib.a: reflectance/rbase/CMakeFiles/rbase-lib.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/fausto/IBTSFIF-master/illuminants/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_13) "Linking CXX static library librbase-lib.a"
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && $(CMAKE_COMMAND) -P CMakeFiles/rbase-lib.dir/cmake_clean_target.cmake
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/rbase-lib.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
reflectance/rbase/CMakeFiles/rbase-lib.dir/build: reflectance/rbase/librbase-lib.a

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/build

reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/shi_db_entry.cpp.o.requires
reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shi.cpp.o.requires
reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_index_shida.cpp.o.requires
reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/db_descriptor.cpp.o.requires
reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read.cpp.o.requires
reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/img_read_config.cpp.o.requires
reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/color_space.cpp.o.requires
reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/mask.cpp.o.requires
reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/illum.cpp.o.requires
reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/color.cpp.o.requires
reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/commands/command_srgb2rgb.cpp.o.requires
reflectance/rbase/CMakeFiles/rbase-lib.dir/requires: reflectance/rbase/CMakeFiles/rbase-lib.dir/srgb2rgb_config.cpp.o.requires

.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/requires

reflectance/rbase/CMakeFiles/rbase-lib.dir/clean:
	cd /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase && $(CMAKE_COMMAND) -P CMakeFiles/rbase-lib.dir/cmake_clean.cmake
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/clean

reflectance/rbase/CMakeFiles/rbase-lib.dir/depend:
	cd /home/fausto/IBTSFIF-master/illuminants/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/fausto/IBTSFIF-master/illuminants /home/fausto/IBTSFIF-master/illuminants/rbase /home/fausto/IBTSFIF-master/illuminants/build /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase /home/fausto/IBTSFIF-master/illuminants/build/reflectance/rbase/CMakeFiles/rbase-lib.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : reflectance/rbase/CMakeFiles/rbase-lib.dir/depend

