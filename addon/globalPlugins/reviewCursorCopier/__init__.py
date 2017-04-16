# Review Cursor Copier
# (C) 2017 Tuukka Ojala <tuukka.ojala@gmail.com>
# Distributed under GNU GPL V2

import addonHandler
import api
import globalCommands
import globalPluginHandler
import textInfos
import ui

addonHandler.initTranslation()

def copyReviewUnitToClipboard(unit, copyFrom=None):
    try:
        pos = api.getReviewPosition()
        info = pos.copy()
        info.expand(unit)
        if copyFrom:
            info.setEndPoint(pos, copyFrom)
        copyStatus = info.copyToClipboard()
        assert copyStatus == True
        # Translators: Copying to the clipboard was successful
        ui.message(_("Copied"))
    except:
        # Translators: copying to the clipboard failed
        ui.message(_("Failed to copy"))

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def script_copyLineToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_LINE)
    # Translators: Describes the "copy line to clipboard" command.
    script_copyLineToClipboard.__doc__ = "Copies the line under the review cursor to the clipboard."
    script_copyLineToClipboard.category = globalCommands.SCRCAT_TEXTREVIEW

    def script_copyWordToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_WORD)
    # Translators: Describes the "copy word to clipboard" command.
    script_copyWordToClipboard.__doc__ = "Copies the word under the review cursor to the clipboard."
    script_copyWordToClipboard.category = globalCommands.SCRCAT_TEXTREVIEW

    def script_copyPrecedingLineToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_LINE, copyFrom="endToStart")
    # Translators: Describes the "copy preceding line to clipboard" command.
    script_copyPrecedingLineToClipboard.__doc__ = "Copies the text from the start of the current line to the clipboard."
    script_copyPrecedingLineToClipboard.category = globalCommands.SCRCAT_TEXTREVIEW

    def script_copyRemainingLineToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_LINE, copyFrom="startToStart")
    # Translators: Describes the "copy remaining line to clipboard" command.
    script_copyRemainingLineToClipboard.__doc__ = "Copies the text until the end of the current line to the clipboard."
    script_copyRemainingLineToClipboard.category = globalCommands.SCRCAT_TEXTREVIEW

    def script_copyPrecedingWordToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_WORD, copyFrom="endToStart")
    # Translators: Describes the "copy preceding word to clipboard" command.
    script_copyPrecedingWordToClipboard.__doc__ = "Copies the text from the start of the current word to the clipboard."
    script_copyPrecedingWordToClipboard.category = globalCommands.SCRCAT_TEXTREVIEW

    def script_copyRemainingWordToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_WORD, copyFrom="startToStart")
    # Translators: Describes the "copy remaining word to clipboard" command.
    script_copyRemainingWordToClipboard.__doc__ = "Copies the text until the end of the current word to the clipboard."
    script_copyRemainingWordToClipboard.category = globalCommands.SCRCAT_TEXTREVIEW
