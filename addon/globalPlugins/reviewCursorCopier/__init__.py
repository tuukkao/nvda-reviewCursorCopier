# Review Cursor Copier
# (C) 2017 Tuukka Ojala <tuukka.ojala@gmail.com>
# Distributed under GNU GPL V2

import re

import addonHandler
import api
import globalCommands
import globalPluginHandler
import textInfos
import ui

RE_URL = re.compile(r"[a-zA-Z]+://[^ ]*")

addonHandler.initTranslation()

def copyReviewUnitToClipboard(unit, copyFrom=None):
    try:
        pos = api.getReviewPosition()
        info = pos.copy()
        info.expand(unit)
        if copyFrom:
            info.setEndPoint(pos, copyFrom)
        text = info.clipboardText.strip()
        copyStatus = api.copyToClip(text)
        if not copyStatus:
            raise RuntimeError
        # Translators: Copying to the clipboard was successful.
        ui.message(_("Copied"))
    except:
        # Translators: Copying to the clipboard failed.
        ui.message(_("Failed to copy"))

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = globalCommands.SCRCAT_TEXTREVIEW

    def script_copyLineToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_LINE)
    # Translators: Describes the "copy line to clipboard" command.
    script_copyLineToClipboard.__doc__ = _("Copies the line under the review cursor to the clipboard.")

    def script_copyWordToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_WORD)
    # Translators: Describes the "copy word to clipboard" command.
    script_copyWordToClipboard.__doc__ = _("Copies the word under the review cursor to the clipboard.")

    def script_copyPrecedingLineToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_LINE, copyFrom="endToStart")
    # Translators: Describes the "copy preceding line to clipboard" command.
    script_copyPrecedingLineToClipboard.__doc__ = _("Copies the text from the start of the current line to the clipboard.")

    def script_copyRemainingLineToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_LINE, copyFrom="startToStart")
    # Translators: Describes the "copy remaining line to clipboard" command.
    script_copyRemainingLineToClipboard.__doc__ = _("Copies the text until the end of the current line to the clipboard.")

    def script_copyPrecedingWordToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_WORD, copyFrom="endToStart")
    # Translators: Describes the "copy preceding word to clipboard" command.
    script_copyPrecedingWordToClipboard.__doc__ = _("Copies the text from the start of the current word to the clipboard.")

    def script_copyRemainingWordToClipboard(self, gesture):
        copyReviewUnitToClipboard(textInfos.UNIT_WORD, copyFrom="startToStart")
    # Translators: Describes the "copy remaining word to clipboard" command.
    script_copyRemainingWordToClipboard.__doc__ = _("Copies the text until the end of the current word to the clipboard.")

    def script_copyUrlToClipboard(self, gesture):
        try:
            info = api.getReviewPosition()
            info.expand(textInfos.UNIT_LINE)
            m = RE_URL.search(info.text)
            if not m:
                # Translators: There was no URL on the line under the review
                # cursor.
                ui.message(_("No URL on this line"))
                return
            copyStatus = api.copyToClip(m.group(0))
            if not copyStatus:
                raise RuntimeError
            # Translators: Copying to the clipboard was successful.
            ui.message(_("Copied"))
        except:
            # Translators: Copying to the clipboard failed.
            ui.message(_("Failed to copy"))
    # Translators: Describes the "copy URL to clipboard" command.
    script_copyUrlToClipboard.__doc__ = _("Copies the first URL on the line under the review cursor to the clipboard.")
