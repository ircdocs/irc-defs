# irc-defs Repo Structure
Given that this is a Jekyll site, there's a very particular way this repo's laid out which I'll go through here.

- `_data/`: Contains the data files which make up our tables.
    - `validation/`: Contains 'validation' files which [yamltypes](https://github.com/DanielOaks/yamltypes) uses to validate the data files.
    - `chanmembers.yaml`: Data for Channel Membership Prefixes (`~&@%+`, etc).
    - `chanmodes.yaml`: Data for Channel Modes (`+b dan!*@*`).
    - `chantypes.yaml`: Data for Channel Types (`#+`).
    - `clientcaps.yaml`: Data for Client Capabilities (`userhost-in-names`, `multi-prefix`, etc).
    - `ctcp.yaml`: Data for CTCP Message Types (`ACTION` robe and wizard hat, `DCC` send me a file, etc).
    - `extbans.yaml`: Data for EXTBANs (Extended Bans, banning/excluding by account, etc).
    - `formatting.yaml`: Info about formatting character support in different clients.
    - `isupport.yaml`: Data for `RPL_ISUPPORT` tokens (`NICKLEN`, `NETWORK=`, etc).
    - `numerics.yaml`: Data for Numerics (`005` == `RPL_ISUPPORT`, etc).
    - `selfmessage.yaml`: Info about self-message support in different clients.
    - `snomasks.yaml`: Data for Server Notice Masks (usually for opers).
    - `stats.yaml`: Data for `STATS` characters.
    - `tags.yaml`: Data for Message Tags (`time=`, `+react`, etc).
    - `usermodes.yaml`: Data for User Modes (`+i`, etc),
- `_includes/`: Contains Jekyll HTML includes.
- `_layouts/`: Contains Jekyll HTML layouts.
- `_legacy_data/`: Contains the original data files from [Alient.net.au](https://www.alien.net.au/irc/) which we used, along with our original conversion script.
- `defs/`: Contains the front-end HTML for each definitions page.
- `info/`: Contains the front-end HTML for each info page.
- `discover_numerics`: Script to discover numerics for various IRC servers from their source repo.

## YAML Structure
To interpret YAML data files:

...todo...
