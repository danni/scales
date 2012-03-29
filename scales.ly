\header {
  title = "Scales"
}

Major = \relative c' { c d e f g a b c }
HarMinor = \relative c' { a b c d e f gis a }
MelMinor = \relative c' { a b c d e fis gis a }
Blues = \relative c' { c d ees f fis g bes c }
Dorian = \relative c' { c d ees f g a bes c }
Lydian = \relative c' { c d e fis g a b c }
Mixolydian = \relative c' { c d e f g a bes c }
Pentatonic = \relative c' { c d e g a c }

\include "scales-include.ly"

% \layout { ragged-right = ##t
%   \context { \Staff
%     \remove "Time_signature_engraver" }
% }
