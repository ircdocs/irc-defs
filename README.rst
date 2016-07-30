IRC Defs
========
These are IRC definition lists. Things like lists of IRC numerics, channel modes, user modes, and other things that are implemented in various bits of IRC software.

Base data was taken from `alien.net.au <https://www.alien.net.au/irc/>`_, converted to YAML via the tools in the ``_legacy_data`` folder, and adapted for use with the `Jekyll <http://jekyllrb.com/>`_ static site generator (used by Github Pages).

Pull requests to correct or update these lists are welcomed.

`Online Site <http://defs.ircdocs.horse/>`_


Available Pages
---------------
* `IRC Numerics <http://defs.ircdocs.horse/defs/numerics.html>`_
* `User Modes <http://defs.ircdocs.horse/defs/usermodes.html>`_
* `Channel Modes <http://defs.ircdocs.horse/defs/chanmodes.html>`_
* `Channel Member Prefixes <http://defs.ircdocs.horse/defs/chanmembers.html>`_
* `Channel Type Prefixes <http://defs.ircdocs.horse/defs/chantypes.html>`_
* `RPL_ISUPPORT Tokens <http://defs.ircdocs.horse/defs/isupport.html>`_
* `Client Capabilities <http://defs.ircdocs.horse/defs/clientcaps.html>`_
* `Tags <http://defs.ircdocs.horse/defs/tags.html>`_
* `Server Modes <http://defs.ircdocs.horse/defs/servermodes.html>`_


License
-------
The following license information is from the `alien.net.au <https://www.alien.net.au/irc/>`_ website::

    You may be interested in using the definition files in your own project;
    There are no license restrictions, other than to retain the copyright information.

Copyright information is listed in the specific converted spec files in the ``_data`` folder (as in the original .def files downloaded from `alien.net.au <https://www.alien.net.au/irc/>`_).


Discovering Numerics
--------------------
I've written a script called ``discover_numerics`` that helps me search for numerics that aren't currently listed in our list. It's helpful to use this to search new releases of Hybrid, Insp, Chary, Unreal, etc.

It requires the ``pyyaml`` and ``docopt`` modules and uses Python3. To install the required modules, install Python3, then run::

    pip3 install pyyaml docopt


Usage Examples
%%%%%%%%%%%%%%

Searching a typical numeric.h file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Searching a single ``numeric.h`` file, such as in IRCD-Hybrid, Charybdis, Unreal, etc::

    ./discover_numerics search /path/to/ircd/include/numerics.h

Searching InspIRCd
^^^^^^^^^^^^^^^^^^

Because Insp scatters its numeric definitions all over its source directory, you can't just search a single file. Because of this, you need to search multiple files in the directory like this::

    find /path/to/inspircd/ | grep cpp | xargs ./discover_numerics search

    find /path/to/inspircd/ | grep \\\.h | xargs ./discover_numerics search

----

Numerics will output as lines like this, which makes it simple to grep through the source directory to discover the format and usage of these numerics::

    Could not find numeric: RPL_STATSCLONE (225)
    Could not find numeric: RPL_USINGSSL (275)
    Could not find numeric: RPL_EXEMPTLIST (348)
    Could not find numeric: RPL_ENDOFEXEMPTLIST (349)
    Could not find numeric: RPL_RWHOREPLY (354)
    Could not find numeric: ERR_TARGETTOFAST (439)
    Could not find numeric: ERR_NOSSL (488)
    Could not find numeric: ERR_NOSHAREDCHAN (493)
    Could not find numeric: ERR_LAST_ERR_MSG (504)
