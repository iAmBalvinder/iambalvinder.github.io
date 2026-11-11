"""Generate static OG image (1200x630) and app icons for balvindersingh.com.

Run with the throwaway venv python: .../opencode/ogenv/bin/python scripts/generate_og.py
Reads brand colors from src/styles/global.css tokens (kept in sync manually).
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
BG = (10, 16, 31)        # --color-bg
ACCENT = (45, 212, 191)  # --color-accent
ACCENT_SOFT = (94, 234, 212)  # --color-accent-strong
FG = (230, 235, 244)     # --color-fg
MUTED = (147, 162, 192)  # --color-muted
LINE = (31, 45, 77)      # --color-line

FONT_PATH = "/System/Library/Fonts/HelveticaNeue.ttc"


def font(size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_PATH, size, index=index)


def main() -> None:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # soft radial-ish glow: concentric ellipses with low alpha accents
    glow = Image.new("L", (W, H), 0)
    glow_draw = ImageDraw.Draw(glow)
    for radius in range(520, 0, -20):
        alpha = int(9 * (1 - radius / 520))
        glow_draw.ellipse(
            [980 - radius, -260 - radius, 980 + radius, -260 + radius],
            fill=alpha,
        )
    overlay = Image.new("RGB", (W, H), ACCENT)
    img.paste(overlay, (0, 0), glow)

    # top accent bar
    draw.rectangle([0, 0, W, 4], fill=ACCENT)

    # eyebrow
    eyebrow_font = font(26, index=1)  # bold-ish variant
    draw.text((80, 108), "BALVINDER SINGH", font=eyebrow_font, fill=ACCENT)

    # headlines
    h1_font = font(78)
    h2_font = font(78)
    draw.text((76, 230), "Data foundations.", font=h1_font, fill=FG)
    draw.text((76, 330), "Production AI.", font=h2_font, fill=ACCENT_SOFT)

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

    # favicon / touch icon: rounded dark square with BS monogram
    def monogram(size: int, path: str) -> None:
        s = 4  # supersample
        big = size * s
        icon = Image.new("RGBA", (big, big), (0, 0, 0, 0))
        d = ImageDraw.Draw(icon)
        d.rounded_rectangle([0, 0, big - 1, big - 1], radius=big // 5, fill=BG)
        f = font(int(big * 0.38), index=1)
        text = "BS"
        bbox = d.textbbox((0, 0), text, font=f)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x = (big - tw) / 2 - bbox[0] - big * 0.02
        y = (big - th) / 2 - bbox[1]
        d.text((x, y), text, font=f, fill=FG)
        # accent period, echoing the site wordmark
        dot_r = big * 0.045
        d.ellipse(
            [x + tw + big * 0.035, y + th - dot_r * 2 + big * 0.01,
             x + tw + big * 0.035 + dot_r * 2, y + th + big * 0.01],
            fill=ACCENT,
        )
        icon = icon.resize((size, size), Image.LANCZOS)
        icon.save(path)
        print(f"wrote {path}")

    monogram(512, "public/images/og-icon.png")
    monogram(180, "public/apple-touch-icon.png")
    monogram(32, "public/favicon.png")


if __name__ == "__main__":
    main()
