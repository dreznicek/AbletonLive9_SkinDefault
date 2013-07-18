from Colors import Basic
from Colors import Rgb
from Colors import Pulse
from Colors import Blink
from Colors import BiLed
class Colors:
    class Option:
        Selected = BiLed.AMBER
        Unselected = BiLed.YELLOW_HALF
        On = BiLed.YELLOW
        Off = BiLed.OFF
        Unused = BiLed.OFF

    class List:
        ScrollerOn = BiLed.AMBER
        ScrollerOff = BiLed.AMBER_HALF

    class DefaultButton:
        On = Basic.FULL
        Off = Basic.HALF
        Disabled = Basic.OFF
        Alert = Basic.FULL_BLINK_SLOW

    class DefaultMatrix:
        On = Rgb.WHITE
        Off = Rgb.BLACK

    class Scales:
        Selected = BiLed.YELLOW
        Unselected = BiLed.GREEN_HALF
        FixedOn = BiLed.AMBER
        FixedOff = BiLed.YELLOW_HALF
        Diatonic = BiLed.AMBER
        Chromatic = BiLed.YELLOW_HALF

    class Instrument:
        NoteBase = Rgb.OCEAN
        NoteScale = Rgb.WHITE
        NoteForeign = Rgb.MAGENTA
        NoteInvalid = Rgb.BLACK
        NoteInactive = Rgb.BLACK
        NoteOff = Rgb.BLACK
        Feedback = Rgb.GREEN
        FeedbackRecord = Rgb.RED.shade(1)

    class Recording:
        On = Basic.FULL
        Off = Basic.HALF
        Transition = Basic.FULL_BLINK_FAST

    class Session:
        SceneSelected = BiLed.GREEN
        SceneUnselected = BiLed.OFF
        SceneTriggered = BiLed.GREEN_BLINK_FAST
        ClipStopped = Rgb.AMBER
        ClipStarted = Pulse(Rgb.GREEN.shade(1), Rgb.GREEN, 48)
        ClipRecording = Pulse(Rgb.BLACK, Rgb.RED, 48)
        ClipTriggeredPlay = Blink(Rgb.GREEN, Rgb.BLACK, 24)
        ClipTriggeredRecord = Blink(Rgb.RED, Rgb.BLACK, 24)
        ClipEmpty = Rgb.BLACK
        RecordButton = Rgb.RED.shade(2)

    class Zooming:
        Selected = Rgb.AMBER
        Stopped = Rgb.RED
        Playing = Rgb.GREEN
        Empty = Rgb.BLACK

    class TrackState:
        Common = Rgb.BLACK
        Stopped = Rgb.RED
        Disabled = Basic.OFF

    class DrumGroup:
        PadSelected = Rgb.OCEAN
        PadSelectedNotSoloed = Rgb.OCEAN
        PadFilled = Rgb.YELLOW
        PadEmpty = Rgb.YELLOW.shade(2)
        PadMuted = Rgb.AMBER.shade(1)
        PadMutedSelected = Rgb.OCEAN.shade(1)
        PadSoloed = Rgb.BLUE
        PadSoloedSelected = Rgb.OCEAN.highlight()
        PadInvisible = Rgb.BLACK

    class LoopSelector:
        Playhead = Rgb.GREEN
        PlayheadRecord = Rgb.RED
        SelectedPage = Rgb.OCEAN
        InsideLoop = Rgb.WHITE
        OutsideLoop = Rgb.DARK_GREY

    class NoteEditor:
        Step = Rgb.SKY.highlight()
        StepHighVelocity = Rgb.OCEAN
        StepFullVelocity = Rgb.BLUE
        StepMuted = Rgb.AMBER.shade(2)
        StepEmpty = Rgb.BLACK
        StepDisabled = Rgb.RED.shade(2)
        Playhead = Rgb.GREEN
        PlayheadRecord = Rgb.RED
        QuantizationSelected = BiLed.GREEN
        QuantizationUnselected = BiLed.YELLOW

    class NoteRepeat:
        RateSelected = BiLed.RED
        RateUnselected = BiLed.YELLOW

    class Mixer:
        SoloOn = Rgb.BLUE
        SoloOff = Rgb.DARK_GREY
        MuteOn = Rgb.DARK_GREY
        MuteOff = BiLed.YELLOW
        StopTrack = Rgb.RED
        StoppingTrack = Blink(Rgb.RED, Rgb.BLACK, 24)
        ArmSelected = BiLed.RED
        ArmUnselected = BiLed.RED_HALF

    class Browser:
        Load = BiLed.GREEN
        LoadNext = BiLed.YELLOW
        LoadNotPossible = BiLed.OFF
        Loading = BiLed.OFF

    class MessageBox:
        Cancel = BiLed.GREEN

