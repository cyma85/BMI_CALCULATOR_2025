import gradio as gr

css = """
body {background: linear-gradient(135deg, #f5f8ff, #eef6ff); font-family: Inter, Arial;}
.app-card {background:white; border-radius:16px; box-shadow: 0 8px 30px rgba(13,38,76,0.08); padding:18px;}
"""

def classify_bmi(bmi: float):
    if bmi < 18.5:
        return "Underweight", "#60a5fa"
    elif bmi < 25:
        return "Normal", "#10b981"
    elif bmi < 30:
        return "Overweight", "#f59e0b"
    else:
        return "Obese", "#ef4444"

def calculate_bmi(weight, height, unit):
    try:
        weight = float(weight)
        height = float(height)
    except:
        return "<div class='app-card'>⚠️ Please enter numbers.</div>"

    if unit.startswith("Metric"):
        height_m = height / 100
        bmi = weight / (height_m * height_m)
    else:
        bmi = (weight / (height * height)) * 703

    bmi = round(bmi, 1)
    label, color = classify_bmi(bmi)
    return f"""
    <div class='app-card'>
      <h2>BMI: {bmi}</h2>
      <div style='padding:6px 10px; background:{color}; color:white; display:inline-block; border-radius:8px'>
        {label}
      </div>
    </div>
    """

with gr.Blocks(css=css, title="BMI Calculator") as demo:
    gr.HTML("<h1 style='text-align:center;color:#0b3d91'>✨ BMI Calculator</h1>")

    with gr.Row():
        with gr.Column():
            weight = gr.Number(value=70, label="Weight")
            height = gr.Number(value=170, label="Height")
            units = gr.Dropdown(
                choices=["Metric (kg, cm)", "Imperial (lb, in)"],
                value="Metric (kg, cm)", label="Units"
            )
            calc_btn = gr.Button("Calculate BMI")
        with gr.Column():
            result_html = gr.HTML("Enter values and click Calculate")

    calc_btn.click(calculate_bmi, [weight, height, units], result_html)

if __name__ == "__main__":
    demo.launch()
