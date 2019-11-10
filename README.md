# IRC Definition Lists

These are IRC definition lists. Things like lists of IRC numerics, channel modes, user modes and other things that are implemented in various bits of IRC software.

Base data was taken from [alien.net.au](https://www.alien.net.au/irc/), converted to YAML via the tools in the `_legacy_data/` folder and adapted for use with the [Jekyll](https://jekyllrb.com/) static site generator (used by Github Pages).

Pull requests to correct or update these lists are welcomed.

Online Site: https://defs.ircdocs.horse/

## Available Pages

* [Channel Member Prefixes](https://defs.ircdocs.horse/defs/chanmembers.html)
* [Channel Modes](https://defs.ircdocs.horse/defs/chanmodes.html)
* [Channel Type Prefixes](https://defs.ircdocs.horse/defs/chantypes.html)
* [Client Capabilities](https://defs.ircdocs.horse/defs/clientcaps.html)
* [CTCP Messages](https://defs.ircdocs.horse/defs/ctcp.html)
* [Extended Bans](https://defs.ircdocs.horse/defs/extban.html)
* [Formatting Characters](https://defs.ircdocs.horse/defs/formatting.html)
* [RPL_ISUPPORT Tokens](https://defs.ircdocs.horse/defs/isupport.html)
* [Numerics](https://defs.ircdocs.horse/defs/numerics.html)
* [self-message](https://defs.ircdocs.horse/defs/selfmessage.html)
* [Server Modes](https://defs.ircdocs.horse/defs/servermodes.html)
* [Server Notice Masks](https://defs.ircdocs.horse/defs/snomasks.html)
* [STATS Characters](https://defs.ircdocs.horse/defs/stats.html)
* [Message Tags](https://defs.ircdocs.horse/defs/tags.html)
* [User Modes](https://defs.ircdocs.horse/defs/usermodes.html)

## Repo Structure

Given that this is a Jekyll site, there's a very particular way this repo is laid out, which I'll go through here:

* `_data/` - contains the data files, which make up our tables;
  * `validation/` - contains validation files, which [yamltypes](https://github.com/DanielOaks/yamltypes) uses to validate the data files;
  * `chanmembers.yaml` - data for Channel Member Prefixes;
  * `chanmodes.yaml` - data for Channel Modes;
  * `chantypes.yaml` - data for Channel Type Prefixes;
  * `clientcaps.yaml` - data for Client Capabilities;
  * `ctcp.yaml` - data for CTCP Messages;
  * `extbans.yaml` - data for Extended Bans (banning/excluding by account, etc.);
  * `formatting.yaml` - data for Formatting Characters support in different clients;
  * `isupport.yaml` - data for `RPL_ISUPPORT` Tokens;
  * `numerics.yaml` - data for Numerics;
  * `selfmessage.yaml` - data for self-message support in different clients;
  * `servermodes.yaml` - data for Server Modes;
  * `snomasks.yaml` - data for Server Notice Masks;
  * `stats.yaml` - data for `STATS` Characters;
  * `tags.yaml` - data for Message Tags;
  * `usermodes.yaml` - data for User Modes;
* `_includes/` - contains Jekyll HTML includes;
  * `table.html` - this is the main data-table printer, outputs based on the content of the YAML data files;
* `_layouts/` - contains Jekyll HTML layouts;
* `_legacy_data/` - contains the original data files from [alient.net.au](https://www.alien.net.au/irc/), which we used, along with our original conversion script;
* `defs/` - contains the front-end HTML for each definitions page;
* `discover_numerics` - script to discover numerics for various IRC servers from their source repo.

## YAML Structure

To interpret YAML data files:

//TODO

## License

The following license information is from the [alien.net.au](https://www.alien.net.au/irc/) website:
```
You may be interested in using the definition files in your own project;
There are no license restrictions, other than to retain the copyright information.
```
Copyright information is listed in the specific converted spec files in the `_data/` folder (as in the original `.def` files downloaded from [alien.net.au](https://www.alien.net.au/irc/)).

## Discovering Numerics

I've written a script called `discover_numerics` that helps me search for numerics that aren't currently listed in our list. It's helpful to use this to search new releases of ircd-hybrid, inspircd, charybdis, unrealircd, etc.

It requires the `pyyaml` and `docopt` python modules. To install the required modules, install `python3-pip`, then run:
```
pip3 install pyyaml docopt
```

### Usage Examples

#### Searching a typical `numeric.h` file

Searching a single `numeric.h` file, such as in ircd-hybrid, charybdis, unrealircd, etc:
```
./discover_numerics search /path/to/ircd/include/numerics.h
```

#### Searching InspIRCd

Because inspircd scatters its numeric definitions all over its source directory, you can't just search a single file. Because of this, you need to search multiple files in the directory like this:

`find /path/to/inspircd/ -type f | xargs ./discover_numerics search`

This also does not find every numeric, thanks to how inspircd likes to use numerics directly rather than `#define` them.

Numerics will output as lines like this, which makes it simple to grep through the source directory to discover the format and usage of these numerics:
```
Could not find numeric: RPL_STATSCLONE (225)
Could not find numeric: RPL_USINGSSL (275)
Could not find numeric: RPL_EXEMPTLIST (348)
Could not find numeric: RPL_ENDOFEXEMPTLIST (349)
Could not find numeric: RPL_RWHOREPLY (354)
Could not find numeric: ERR_TARGETTOFAST (439)
Could not find numeric: ERR_NOSSL (488)
Could not find numeric: ERR_NOSHAREDCHAN (493)
Could not find numeric: ERR_LAST_ERR_MSG (504)
```
