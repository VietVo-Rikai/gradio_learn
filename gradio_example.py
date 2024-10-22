import gradio as gr

# Hàm tính bình phương
def square(x):
    return x ** 2

# Tạo giao diện với ô nhập và kết quả đầu ra
iface = gr.Interface(fn=square, inputs="number", outputs="text")

# Khởi chạy giao diện
iface.launch()
