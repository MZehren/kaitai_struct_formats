meta:
  id: guitar_pro_5
  application: Guitar Pro 5
  file-extension: gp5
  xref:
    justsolve: Guitar_Pro_4
  license: MIT
  endian: le
doc: |
  Guitar Pro is a very common software to transcribe music. TODO 
  blabla
seq:
  - id: version
    type: byte_str
    size: 31
  - id: title
    type: int_byte_str
  - id: transcribed
    type: int_byte_str
  #   size-eos: true
# instances:
types:
  byte_str:
    seq:
      - id: len
        type: s1
      - id: value
        type: str
        encoding: UTF-8
        size: len
    doc: bla
  int_byte_str:
    seq:
      - id: len
        type: s4
      - id: value
        type: byte_str
        size: len
    doc: blablabla
    
# enums: