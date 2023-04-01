# This file is generated by objective.metadata
#
# Last update: Thu Jul  7 22:06:46 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$$"""
enums = """$QLPreviewViewStyleCompact@1$QLPreviewViewStyleNormal@0$"""
misc.update({"QLPreviewViewStyle": NewType("QLPreviewViewStyle", int)})
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSObject",
        b"acceptsPreviewPanelControl:",
        {"retval": {"type": b"Z"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"beginPreviewPanelControl:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"endPreviewPanelControl:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"numberOfPreviewItemsInPreviewPanel:",
        {"required": True, "retval": {"type": b"q"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"preparePreviewOfFileAtURL:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": "@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"preparePreviewOfSearchableItemWithIdentifier:queryString:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {0: {"type": b"^v"}, 1: {"type": b"@"}},
                    },
                    "type": "@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"previewItemDisplayState",
        {"required": False, "retval": {"type": b"@"}},
    )
    r(b"NSObject", b"previewItemTitle", {"required": False, "retval": {"type": b"@"}})
    r(b"NSObject", b"previewItemURL", {"required": True, "retval": {"type": b"@"}})
    r(
        b"NSObject",
        b"previewPanel:handleEvent:",
        {
            "required": False,
            "retval": {"type": b"Z"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"previewPanel:previewItemAtIndex:",
        {
            "required": True,
            "retval": {"type": b"@"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"q"}},
        },
    )
    r(
        b"NSObject",
        b"previewPanel:sourceFrameOnScreenForPreviewItem:",
        {
            "required": False,
            "retval": {"type": b"{CGRect={CGPoint=dd}{CGSize=dd}}"},
            "arguments": {2: {"type": b"@"}, 3: {"type": b"@"}},
        },
    )
    r(
        b"NSObject",
        b"previewPanel:transitionImageForPreviewItem:contentRect:",
        {
            "required": False,
            "retval": {"type": b"@"},
            "arguments": {
                2: {"type": b"@"},
                3: {"type": b"@"},
                4: {
                    "type": b"^{CGRect={CGPoint=dd}{CGSize=dd}}",
                    "type_modifier": b"n",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"providePreviewForFileRequest:completionHandler:",
        {
            "required": False,
            "retval": {"type": b"v"},
            "arguments": {
                2: {"type": b"@"},
                3: {
                    "callable": {
                        "retval": {"type": b"v"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"@"},
                        },
                    },
                    "type": b"@?",
                },
            },
        },
    )
    r(
        b"NSObject",
        b"setPreviewItemDisplayState:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setPreviewItemTitle:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setPreviewItemURL:",
        {"retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"QLPreviewPanel",
        b"enterFullScreenMode:withOptions:",
        {"retval": {"type": b"Z"}},
    )
    r(b"QLPreviewPanel", b"isInFullScreenMode", {"retval": {"type": b"Z"}})
    r(b"QLPreviewPanel", b"sharedPreviewPanelExists", {"retval": {"type": b"Z"}})
    r(
        b"QLPreviewReply",
        b"initForPDFWithPageSize:documentCreationBlock:",
        {
            "arguments": {
                3: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"o^@"},
                        },
                    }
                }
            }
        },
    )
    r(
        b"QLPreviewReply",
        b"initWithContextSize:isBitmap:drawingBlock:",
        {
            "arguments": {
                3: {"type": b"Z"},
                4: {
                    "callable": {
                        "retval": {"type": b"Z"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"^{CGContext=}"},
                            2: {"type": b"@"},
                            3: {"type": b"o^@"},
                        },
                    }
                },
            }
        },
    )
    r(
        b"QLPreviewReply",
        b"initWithDataOfContentType:contentSize:dataCreationBlock:",
        {
            "arguments": {
                4: {
                    "callable": {
                        "retval": {"type": b"@"},
                        "arguments": {
                            0: {"type": b"^v"},
                            1: {"type": b"@"},
                            2: {"type": b"o^@"},
                        },
                    }
                }
            }
        },
    )
    r(b"QLPreviewView", b"autostarts", {"retval": {"type": b"Z"}})
    r(b"QLPreviewView", b"setAutostarts:", {"arguments": {2: {"type": b"Z"}}})
    r(
        b"QLPreviewView",
        b"setShouldCloseWithWindow:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"QLPreviewView", b"shouldCloseWithWindow", {"retval": {"type": b"Z"}})
finally:
    objc._updatingMetadata(False)
protocols = {
    "QLPreviewPanelController": objc.informal_protocol(
        "QLPreviewPanelController",
        [
            objc.selector(
                None, b"beginPreviewPanelControl:", b"v@:@", isRequired=False
            ),
            objc.selector(
                None, b"acceptsPreviewPanelControl:", b"Z@:@", isRequired=False
            ),
            objc.selector(None, b"endPreviewPanelControl:", b"v@:@", isRequired=False),
        ],
    )
}
expressions = {}

# END OF FILE