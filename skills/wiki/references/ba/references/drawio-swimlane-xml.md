# Draw.io Swimlane XML Templates

## Purpose
Use during diagram generation in ba-process-modeler.
Copy and adapt these XML blocks. All coordinates are relative starting points — adjust x/y for actual layout.
All XML must be wrapped in the standard Draw.io document envelope below.

---

## Document Envelope

Every Draw.io file starts and ends with this structure:

```xml
<mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1" tooltips="1"
  connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1654"
  pageHeight="1169" math="0" shadow="0">
  <root>
    <mxCell id="0"/>
    <mxCell id="1" parent="0"/>
    <!-- ALL CONTENT GOES HERE -->
  </root>
</mxGraphModel>
```

---

## Pool Container (outer boundary)

```xml
<mxCell id="pool-1" value="[Pool Name / Organisation]"
  style="shape=pool;startSize=20;horizontal=1;childLayout=stackLayout;horizontalStack=0;
         resizeParent=1;resizeParentMax=0;horizontalStack=0;fillColor=#f5f5f5;
         strokeColor=#666666;fontColor=#333333;fontStyle=1;fontSize=14;"
  vertex="1" parent="1">
  <mxGeometry x="40" y="40" width="1600" height="400" as="geometry"/>
</mxCell>
```

---

## Swimlane (inside pool)

First lane — y offset 20 (below pool header):
```xml
<mxCell id="lane-1" value="[Role / Actor Name]"
  style="swimlane;startSize=30;horizontal=0;fillColor=#dae8fc;strokeColor=#6c8ebf;
         fontStyle=1;fontSize=12;"
  vertex="1" parent="pool-1">
  <mxGeometry y="20" width="1600" height="120" as="geometry"/>
</mxCell>
```

Subsequent lanes — increment y by 120 per lane:
```xml
<mxCell id="lane-2" value="[Second Role]"
  style="swimlane;startSize=30;horizontal=0;fillColor=#e1d5e7;strokeColor=#9673a6;
         fontStyle=1;fontSize=12;"
  vertex="1" parent="pool-1">
  <mxGeometry y="140" width="1600" height="120" as="geometry"/>
</mxCell>
```

---

## Start Event

```xml
<mxCell id="start-1" value="[Trigger Label]"
  style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#d5e8d4;strokeColor=#82b366;
         fontSize=11;fontStyle=0;strokeWidth=1;"
  vertex="1" parent="lane-1">
  <mxGeometry x="60" y="40" width="50" height="50" as="geometry"/>
</mxCell>
```

---

## End Event

```xml
<mxCell id="end-1" value="[Outcome Label]"
  style="ellipse;whiteSpace=wrap;html=1;aspect=fixed;fillColor=#f8cecc;strokeColor=#b85450;
         fontSize=11;fontStyle=0;strokeWidth=3;"
  vertex="1" parent="lane-1">
  <mxGeometry x="1480" y="40" width="50" height="50" as="geometry"/>
</mxCell>
```

---

## Human Task

```xml
<mxCell id="task-1" value="[Verb + Noun]"
  style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#dae8fc;strokeColor=#6c8ebf;
         fontSize=12;fontStyle=0;"
  vertex="1" parent="lane-1">
  <mxGeometry x="160" y="35" width="140" height="60" as="geometry"/>
</mxCell>
```

---

## System / Automated Task

```xml
<mxCell id="task-sys-1" value="[System Action]"
  style="rounded=1;whiteSpace=wrap;html=1;arcSize=20;fillColor=#e1d5e7;strokeColor=#9673a6;
         fontSize=12;fontStyle=0;"
  vertex="1" parent="lane-2">
  <mxGeometry x="160" y="35" width="140" height="60" as="geometry"/>
</mxCell>
```

---

## XOR Gateway (Exclusive — Decision)

```xml
<mxCell id="gw-1" value="[Decision Question]"
  style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;
         fontSize=11;fontStyle=1;verticalAlign=middle;"
  vertex="1" parent="lane-1">
  <mxGeometry x="360" y="30" width="70" height="70" as="geometry"/>
</mxCell>
```

---

## AND Gateway (Parallel)

```xml
<mxCell id="gw-and-1" value="+"
  style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;
         fontSize=18;fontStyle=1;verticalAlign=middle;"
  vertex="1" parent="lane-1">
  <mxGeometry x="360" y="30" width="70" height="70" as="geometry"/>
</mxCell>
```

---

## Sequence Flow Arrow

Unlabelled (within same lane):
```xml
<mxCell id="flow-1" style="edgeStyle=orthogonalEdgeStyle;html=1;exitX=1;exitY=0.5;
         entryX=0;entryY=0.5;strokeColor=#000000;endArrow=block;endFill=1;"
  edge="1" source="task-1" target="task-2" parent="pool-1">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

Labelled gateway branch (Yes):
```xml
<mxCell id="flow-yes" value="Yes"
  style="edgeStyle=orthogonalEdgeStyle;html=1;exitX=1;exitY=0.5;
         entryX=0;entryY=0.5;strokeColor=#000000;endArrow=block;endFill=1;
         fontSize=11;fontStyle=1;"
  edge="1" source="gw-1" target="task-2" parent="pool-1">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

Labelled gateway branch (No — typically routes downward):
```xml
<mxCell id="flow-no" value="No"
  style="edgeStyle=orthogonalEdgeStyle;html=1;exitX=0.5;exitY=1;
         entryX=0.5;entryY=0;strokeColor=#000000;endArrow=block;endFill=1;
         fontSize=11;fontStyle=1;"
  edge="1" source="gw-1" target="task-3" parent="pool-1">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

---

## Sub-Process (Collapsed)

```xml
<mxCell id="sub-1" value="[Sub-Process Name]"
  style="rounded=1;whiteSpace=wrap;html=1;arcSize=10;fillColor=#f5f5f5;strokeColor=#666666;
         fontSize=12;fontStyle=0;spacingBottom=18;"
  vertex="1" parent="lane-1">
  <mxGeometry x="160" y="30" width="160" height="70" as="geometry"/>
</mxCell>
<!-- Sub-process [+] marker -->
<mxCell id="sub-1-marker" value="+"
  style="text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;
         fontSize=14;fontStyle=1;"
  vertex="1" parent="lane-1">
  <mxGeometry x="228" y="85" width="24" height="14" as="geometry"/>
</mxCell>
```

---

## Pain Point Hotspot Annotation

```xml
<mxCell id="hotspot-1" value="[Pain Point Description]"
  style="rounded=1;whiteSpace=wrap;html=1;fillColor=#ffe6cc;strokeColor=#d79b00;
         fontSize=10;fontStyle=2;"
  vertex="1" parent="lane-1">
  <mxGeometry x="155" y="5" width="150" height="30" as="geometry"/>
</mxCell>
<!-- Association line from hotspot to task -->
<mxCell id="assoc-1"
  style="edgeStyle=none;html=1;dashed=1;endArrow=none;strokeColor=#d79b00;"
  edge="1" source="hotspot-1" target="task-1" parent="pool-1">
  <mxGeometry relative="1" as="geometry"/>
</mxCell>
```

---

## Layout Guidance

**Horizontal spacing between tasks:** 60px gap between right edge of one task and left edge of next
**Task dimensions:** 140px wide × 60px tall (standard); 180px wide for longer labels
**Gateway positioning:** Gateway x = preceding task x + 140 + 60
**Next task after gateway (yes path):** Gateway x + 70 + 60
**Cross-lane routing:** Use orthogonal edge style; the edge will route through the pool container

**Multi-page file (AS-IS + TO-BE):**
The mxGraphModel tag should be inside a `<diagram>` tag for each page:
```xml
<mxfile>
  <diagram id="as-is" name="AS-IS">
    <mxGraphModel>...</mxGraphModel>
  </diagram>
  <diagram id="to-be" name="TO-BE">
    <mxGraphModel>...</mxGraphModel>
  </diagram>
</mxfile>
```
