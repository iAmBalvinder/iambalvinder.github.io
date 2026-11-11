"""Generate static OG image (1200x630) and app icons for balvindersingh.com.

Light editorial palette matching src/styles/global.css tokens.
Run with the throwaway venv python: .../opencode/ogenv/bin/python scripts/generate_og.py
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
PAPER = (250, 248, 244)      # --bg (light)
INK = (28, 26, 23)           # --fg (light)
MUTED = (111, 105, 94)       # --muted (light)
ACCENT = (31, 92, 63)        # --accent (light)

FONT_PATH = "/System/Library/Fonts/HelveticaNeue.ttc"


def font(size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size, index=index)


def main() -> None:
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # top accent bar
    draw.rectangle([0, 0, W, 6], fill=ACCENT)
    # bottom hairline
    draw.rectangle([0, H - 2, W, H], fill=INK)

    # eyebrow
    eyebrow_font = font(26, index=1)
    draw.text((80, 112), "BALVINDER SINGH", font=eyebrow_font, fill=ACCENT)

    # headlines
    h1_font = font(80)
    draw.text((76, 225), "Data foundations.", font=h1_font, fill=INK)
    draw.text((76, 325), "Production AI.", font=h1_font, fill=ACCENT)

    # subline
    sub_font = font(30)
    draw.text(
        (80, 470),
        "Data engineering to LLM & AI engineering - consulting",
        font=sub_font,
        fill=MUTED,
    )

    img.save("public/images/og-default.png", optimize=True)
    print("wrote public/images/og-default.png")

    # favicon / touch icon: ink rounded square, paper BS monogram, green dot
    def monogram(size: int, path: str) -> None:
        s = 4  # supersample
        big = size * s
        icon = Image.new("RGBA", (big, big), (0, 0, 0, 0))
        d = ImageDraw.Draw(icon)
        d.rounded_rectangle([0, 0, big - 1, big - 1], radius=big // 5, fill=INK)
        f = font(int(big * 0.38), index=1)
        text = "BS"
        bbox = d.textbbox((0, 0), text, font=f)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x = (big - tw) / 2 - bbox[0] - big * 0.02
        y = (big - th) / 2 - bbox[1]
        d.text((x, y), text, font=f, fill=PAPER)
        # green period, echoing the site wordmark
        dot_r = big * 0.045
        d.ellipse(
            [x + tw + big * 0.035, y + th - dot_r * 2 + big * 0.01,
             x + tw + big * 0.035 + dot_r * 2, y + th + big * 0.01],
            fill=(76, 168, 125),
        )
        icon = icon.resize((size, size), Image.LANCZOS)
        icon.save(path)
        print(f"wrote {path}")

    monogram(512, "public/images/og-icon.png")
    monogram(180, "public/apple-touch-icon.png")
    monogram(32, "public/favicon.png")


if __name__ == "__main__":
    main()
