/*****************************************************************************
 * GENERATED CLASS - ALL CHANGES ARE LOST AFTER RECONFIGURATION OF THE VOLE
 * PROJECT.
 *
 * DO NOT EDIT THIS FILE (UNLESS YOU REALLY KNOW WHAT YOU DO) - IF IT DOES NOT
 * SUIT YOUR NEEDS, CHANGE THE APPROPRIATE VOLE COMPONENT THAT LEFT ITS TRACES
 * HERE!
 ****************************************************************************/

#include "modules.h"

namespace vole {

Modules::Modules() {
	Command *c;

	/* Algorithms for Superpixel Segmentation */
	c = new vole::CommandVeksler(); insert(std::make_pair(c->getName(), c));

}

}
