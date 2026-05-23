#let style(header: none, body) = {
  // Configuraciones generales
  set text(font: "Lato", size: 11pt, lang: "es")
  set page(
    margin: (x: 2.5cm, y: 3cm),
    header: align(
      right,
      text(size: 9pt, fill: gray, style: "italic", if header != none { header }),
    ),
  )

  // Título 1: Centrado y destacado
  show heading.where(level: 1): it => block(
    above: 1.5em,
    below: 1em,
    align(center, text(size: 1.3em, weight: "bold", it.body)),
  )

  // Títulos 2 y 3: Alineados a la izquierda
  show heading.where(level: 2): it => block(
    above: 1.5em,
    below: 1em,
    text(size: 1.2em, weight: "semibold", it.body),
  )

  show heading.where(level: 3): it => block(
    above: 1.5em,
    below: 1em,
    text(size: 1.1em, weight: "semibold", it.body),
  )

  // Bloques de citas
  show quote: set text(style: "italic")
  show quote.where(block: true): block.with(
    stroke: (left: 2pt + gray, rest: none),
    inset: (y: 0.5em),
    outset: (left: 0em),
  )

  // Bloques de código
  show raw: set text(font: "Google Sans Code")
  set raw(tab-size: 4)

  body
}

// Callout
#let callout(color: rgb("#ffffff00"), body) = rect(
  width: 100%,
  fill: color,
  stroke: 1pt,
  radius: 10pt,
  inset: 10pt,
  body,
)
