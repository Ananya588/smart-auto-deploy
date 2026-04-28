from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Smart Auto Deploy is launching soon.">
    <title>Smart Auto Deploy | Coming Soon</title>
    <style>
        :root {
            color-scheme: dark;
            --bg: #10131a;
            --panel: rgba(18, 23, 33, 0.78);
            --panel-border: rgba(255, 255, 255, 0.16);
            --text: #f8fafc;
            --muted: #b7c0cc;
            --accent: #38bdf8;
            --accent-strong: #2dd4bf;
            --warning: #f59e0b;
        }

        * {
            box-sizing: border-box;
        }

        html,
        body {
            min-height: 100%;
        }

        body {
            margin: 0;
            font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            color: var(--text);
            background:
                radial-gradient(circle at 18% 22%, rgba(56, 189, 248, 0.26), transparent 30%),
                radial-gradient(circle at 82% 12%, rgba(45, 212, 191, 0.18), transparent 28%),
                linear-gradient(135deg, #10131a 0%, #16202a 52%, #0f1720 100%);
            overflow-x: hidden;
        }

        body::before {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            background-image:
                linear-gradient(rgba(255, 255, 255, 0.045) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255, 255, 255, 0.045) 1px, transparent 1px);
            background-size: 48px 48px;
            mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.9), transparent 78%);
        }

        .page {
            min-height: 100vh;
            display: grid;
            place-items: center;
            padding: 32px 18px;
        }

        .shell {
            width: min(1040px, 100%);
            display: grid;
            grid-template-columns: minmax(0, 1.15fr) minmax(280px, 0.85fr);
            gap: 28px;
            align-items: stretch;
        }

        .hero,
        .status-panel {
            border: 1px solid var(--panel-border);
            background: var(--panel);
            box-shadow: 0 24px 90px rgba(0, 0, 0, 0.38);
            backdrop-filter: blur(18px);
        }

        .hero {
            min-height: 560px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: clamp(28px, 5vw, 56px);
            border-radius: 8px;
            position: relative;
            overflow: hidden;
        }

        .hero::after {
            content: "";
            position: absolute;
            right: -120px;
            bottom: -160px;
            width: 380px;
            height: 380px;
            border: 1px solid rgba(56, 189, 248, 0.24);
            transform: rotate(18deg);
            border-radius: 32px;
        }

        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 0.92rem;
            font-weight: 700;
            letter-spacing: 0;
            text-transform: uppercase;
            color: #dbeafe;
        }

        .mark {
            width: 36px;
            height: 36px;
            display: grid;
            place-items: center;
            border-radius: 8px;
            color: #07111f;
            background: linear-gradient(135deg, var(--accent), var(--accent-strong));
            font-weight: 900;
        }

        .content {
            max-width: 680px;
            position: relative;
            z-index: 1;
        }

        .eyebrow {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            margin: 0 0 18px;
            color: #bfdbfe;
            font-size: 0.9rem;
            font-weight: 700;
        }

        .dot {
            width: 10px;
            height: 10px;
            border-radius: 999px;
            background: var(--warning);
            box-shadow: 0 0 24px rgba(245, 158, 11, 0.8);
        }

        h1 {
            margin: 0;
            max-width: 760px;
            font-size: clamp(3rem, 8vw, 6.8rem);
            line-height: 0.92;
            letter-spacing: 0;
        }

        .lede {
            max-width: 650px;
            margin: 26px 0 0;
            color: var(--muted);
            font-size: clamp(1.02rem, 2vw, 1.22rem);
            line-height: 1.7;
        }

        .actions {
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            margin-top: 34px;
        }

        .pill {
            min-height: 44px;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 10px 16px;
            border: 1px solid rgba(255, 255, 255, 0.16);
            border-radius: 999px;
            color: #e5edf6;
            background: rgba(255, 255, 255, 0.07);
            font-size: 0.92rem;
            font-weight: 700;
        }

        .pill strong {
            color: white;
        }

        .footer-note {
            position: relative;
            z-index: 1;
            color: #93a4b7;
            font-size: 0.92rem;
        }

        .status-panel {
            min-height: 560px;
            border-radius: 8px;
            padding: 28px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .panel-title {
            margin: 0 0 18px;
            color: #e2e8f0;
            font-size: 1rem;
            font-weight: 800;
        }

        .pipeline {
            display: grid;
            gap: 14px;
        }

        .step {
            display: grid;
            grid-template-columns: 34px 1fr;
            gap: 12px;
            align-items: start;
            padding: 16px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.05);
        }

        .step-index {
            width: 34px;
            height: 34px;
            display: grid;
            place-items: center;
            border-radius: 8px;
            color: #06101c;
            background: #bae6fd;
            font-weight: 900;
        }

        .step h2 {
            margin: 0;
            font-size: 1rem;
            letter-spacing: 0;
        }

        .step p {
            margin: 6px 0 0;
            color: var(--muted);
            font-size: 0.92rem;
            line-height: 1.5;
        }

        .availability {
            margin-top: 26px;
            padding-top: 22px;
            border-top: 1px solid rgba(255, 255, 255, 0.12);
        }

        .meter {
            height: 10px;
            overflow: hidden;
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.12);
        }

        .meter span {
            display: block;
            width: 72%;
            height: 100%;
            border-radius: inherit;
            background: linear-gradient(90deg, var(--accent), var(--accent-strong));
        }

        .caption {
            display: flex;
            justify-content: space-between;
            gap: 16px;
            margin-top: 10px;
            color: #cbd5e1;
            font-size: 0.86rem;
            font-weight: 700;
        }

        @media (max-width: 820px) {
            .page {
                display: block;
                padding: 18px;
            }

            .shell {
                grid-template-columns: 1fr;
            }

            .hero,
            .status-panel {
                min-height: auto;
            }

            .hero {
                gap: 76px;
            }
        }

        @media (max-width: 520px) {
            h1 {
                font-size: clamp(2.6rem, 17vw, 4rem);
            }

            .hero,
            .status-panel {
                padding: 22px;
            }

            .actions,
            .caption {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <main class="page">
        <section class="shell" aria-label="Launch status">
            <div class="hero">
                <div class="brand">
                    <span class="mark">S</span>
                    <span>Smart Auto Deploy</span>
                </div>

                <div class="content">
                    <p class="eyebrow"><span class="dot"></span> Deployment pipeline warming up</p>
                    <h1>Coming Soon</h1>
                    <p class="lede">
                        A smarter release experience is being prepared. The instance is live,
                        the application is reachable, and the next production build is on its way.
                    </p>

                    <div class="actions" aria-label="Current platform highlights">
                        <span class="pill"><strong>Flask</strong> app online</span>
                        <span class="pill"><strong>ECS</strong> ready</span>
                        <span class="pill"><strong>AWS</strong> hosted</span>
                    </div>
                </div>

                <p class="footer-note">This page will be replaced automatically when the product launch build is deployed.</p>
            </div>

            <aside class="status-panel" aria-label="Release progress">
                <div>
                    <p class="panel-title">Launch Checklist</p>
                    <div class="pipeline">
                        <article class="step">
                            <div class="step-index">1</div>
                            <div>
                                <h2>Infrastructure</h2>
                                <p>Cloud resources are provisioned and ready to receive traffic.</p>
                            </div>
                        </article>

                        <article class="step">
                            <div class="step-index">2</div>
                            <div>
                                <h2>Container</h2>
                                <p>The application image is built, pushed, and prepared for rollout.</p>
                            </div>
                        </article>

                        <article class="step">
                            <div class="step-index">3</div>
                            <div>
                                <h2>Release</h2>
                                <p>The public experience is being finalized before launch.</p>
                            </div>
                        </article>
                    </div>
                </div>

                <div class="availability">
                    <div class="meter" aria-hidden="true"><span></span></div>
                    <div class="caption">
                        <span>Launch progress</span>
                        <span>Preparing final rollout</span>
                    </div>
                </div>
            </aside>
        </section>
    </main>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML_PAGE)


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
