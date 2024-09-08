import matplotlib.pyplot as plt
import io

def generate_chart(data, chart_type='bar'):
    plt.figure(figsize=(10, 6))
    
    if chart_type == 'bar':
        plt.bar(data.keys(), data.values())
    elif chart_type == 'pie':
        plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
    elif chart_type == 'line':
        plt.plot(list(data.keys()), list(data.values()))
    
    plt.title(f"{chart_type.capitalize()} Chart")
    plt.tight_layout()
    
    # Save the chart to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    plt.close()
    
    return buf
