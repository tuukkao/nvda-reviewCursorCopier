# Review Cursor Copier

* Author: Tuukka Ojala <tuukka.ojala@iki.fi>

This NVDA add-on provides various commands for copying the text under the review cursor to the clipboard. Currently, the following commands are implemented:

* Copy the line under the review cursor
* Copy the word under the review cursor
* Copy from the start of the current line to the review cursor
* Copy from the review cursor to the end of the current line
* Copy from the start of the current word to the review cursor
* Copy from the review cursor to the end of the current word
* Copy the first URL on the line under the review cursor

None of these commands have key bindings by default. Please use the input gestures dialog located under the NVDA preferences menu to set them. All of the commands provided by this add-on can be found under the "text review" category. More information about setting and modifying input gestures can be found in the NVDA user guide.

Note that these commands will trim any preceding and trailing white space from the copied text. This is because lines in command consoles using UI automation contain extra spaces which aren't useful and would need to be removed manually. Please use the standard NVDA+f9 and NVDA+f10 commands if you need to retain white space.

## License

This work is licensed under the GNU General Public License, version 2.
