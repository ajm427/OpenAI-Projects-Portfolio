# Six-Sided Sample Scanner

A low-cost lab intake imaging station designed to photograph **all visible sides of a sample in one placement**, including the bottom, using multiple USB/UVC cameras and a transparent sample platform.

## Goal

Reduce manual sample photography time during intake by replacing repeated handling, rotating, and repositioning with a fixed multi-camera enclosure.

The intended workflow is:

1. Place the sample on a clear glass platform.
2. Scan/enter the sample or test ID.
3. Capture images from six directions: Front, Back, Left, Right, Top, Bottom.
4. Save the image set under the sample/test identifier.
5. Optionally run barcode/QR detection or OCR on the images.
6. Optionally send the resulting image set or status into a lab workflow system through an API.

## Estimated Time & Labor Impact

The table below gives a concrete example of the potential impact. The Python calculator remains configurable for different real-world assumptions.

**Example assumptions:** 100 samples/day, 60 seconds of manual photography per sample, 15 seconds using the scanner, 250 workdays/year, **$22/hour labor**, and a $500 prototype build cost.

| Metric | Estimated Result |
|---|---:|
| Time saved per sample | **45 seconds** |
| Time saved per 100 samples | **75 minutes/day** |
| Labor hours saved per year | **312.5 hours** |
| Equivalent 8-hour workdays recovered | **39.1 days/year** |
| Labor value saved per day | **$27.50** |
| Labor value saved per month | **~$573** |
| Labor value saved per year | **$6,875** |
| Estimated prototype cost | **$500** |
| Estimated payback period | **~18 workdays** |
| First-year net labor savings after build cost | **$6,375** |

These figures are projections rather than measured production results. Actual savings should be recalculated after timing the current manual workflow and the finished prototype.

### Core calculation

```text
Time Saved = Samples × (Manual Seconds − Scanner Seconds)
Annual Labor Value = Annual Hours Saved × Hourly Labor Cost
Payback Period = Build Cost ÷ Daily Labor Value Saved
```

## Proposed Physical Design

Approximate enclosure dimensions:

- Exterior: **22 in W × 22 in D × 28 in H**
- Usable sample chamber: approximately **18 in W × 18 in D × 24 in H**
- Transparent platform: approximately **14 in × 14 in tempered glass**

This size is intentionally conservative so the system can accommodate bottles, pouches, jars, supplement tubs, boxes, and other larger samples.

## Camera Layout

```text
                 TOP CAMERA
                     ↓
          ┌─────────────────────┐
          │                     │
          │       SAMPLE        │
 LEFT  →  │                     │  ← RIGHT
 CAMERA   │                     │    CAMERA
          │                     │
 FRONT →  │                     │  ← BACK
 CAMERA   │                     │    CAMERA
          │  ═══════════════    │
          │    CLEAR GLASS      │
          │         ↑           │
          │    BOTTOM CAMERA    │
          └─────────────────────┘
```

The bottom camera points upward through the glass so the underside can be captured without manually flipping the sample.

## Main Materials

- 2020 aluminum T-slot extrusion frame
- 90° extrusion brackets and M5 T-nuts/bolts
- Black ABS or expanded PVC enclosure panels
- Clear tempered-glass sample platform
- White translucent diffuser material
- High-CRI 5000K LED lighting
- Six autofocus USB/UVC cameras
- Powered USB 3.x hub
- USB-C connection to the host computer
- Door hinges/latch
- Cable management hardware
- Rubber feet

## 3D-Printed Components

The specialized pieces can be printed rather than purchased:

- Adjustable camera carriages
- Sliding camera mounts for 2020 extrusion
- Tilt-adjustment brackets
- Glass corner/platform supports
- LED and diffuser holders
- Cable clips and cable channels
- Powered USB hub bracket
- Door handle
- Sample-centering guides
- Replaceable camera alignment fixtures

A useful design goal is to make each camera carriage slide closer to or farther from the sample. Positions can later be marked as Small / Medium / Large depending on sample size.

## Why Multi-Camera Instead of a Traditional 3D Scanner?

The primary requirement is documentation and label visibility rather than creation of a dimensionally accurate 3D mesh.

A fixed multi-camera system can therefore be faster, less expensive, easier to maintain and integrate, better suited for barcode/OCR workflows, and able to capture the bottom through transparent glass.

## Software Direction

A future application could:

- Detect all connected UVC cameras
- Associate each camera with a fixed direction
- Trigger still-image capture sequentially or simultaneously
- Name files automatically from a scanned sample/test ID
- Verify that six expected images were captured
- Run barcode/QR recognition
- Run OCR for lot number, expiration date, SKU, or product information
- Flag blurry or obstructed images
- Upload or attach images through an API
- Show capture-completeness status in a dashboard

Example output structure:

```text
sample_40654/
├── front.jpg
├── back.jpg
├── left.jpg
├── right.jpg
├── top.jpg
└── bottom.jpg
```

## USB Considerations

Six high-resolution cameras may exceed the practical bandwidth of a single USB controller when streaming video simultaneously. Since this application primarily needs still images, the software can capture cameras sequentially or divide cameras across multiple powered hubs/controllers.

UVC-compatible cameras are preferred because they are broadly supported by macOS and other operating systems without proprietary camera drivers.

## Prototype Strategy

1. Build the aluminum frame and lighting enclosure.
2. Install the glass platform.
3. Test one autofocus UVC camera at the actual working distance.
4. Confirm label readability and glare control.
5. Duplicate the camera configuration across the remaining positions.
6. Add capture software.
7. Add OCR/barcode/API integrations only after the imaging workflow is reliable.

## Time-Savings Calculator

See [`time_savings.py`](./time_savings.py) for the configurable calculator used to model labor hours, labor value, and project payback under different assumptions.
