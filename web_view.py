import json
import matplotlib.pyplot as plt
import pandas as pd


def fetch_data():
    file_path = 'Data/walking/AFE_000_CONFIDENTIAL.json'
    with open(file_path) as json_file:
        data = json.load(json_file)
        #print(data)
    #convert data to json string
    json_string = json.dumps(data)

    # Extracting and plotting data
    left_eye = [sample['afe'][0]['m'][0] for sample in data if sample['afe'][0]]
    right_eye = [sample['afe'][1]['m'][0] for sample in data if sample['afe'][1]]

    # Plotting
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    fig.suptitle('Eye Sensor Data')

    # Left Eye Data
    for i in range(6):  # Plotting first six sensors
        axes[0].plot([sample[i] for sample in left_eye], label=f'Sensor {i+1}')
    axes[0].set_title('Left Eye')
    axes[0].set_xlabel('Sample Index')
    axes[0].set_ylabel('Sensor Value')
    axes[0].legend()
    axes[0].grid(True)

    # Right Eye Data
    for i in range(6):  # Plotting first six sensors
        axes[1].plot([sample[i] for sample in right_eye], label=f'Sensor {i+1}', color='green')
    axes[1].set_title('Right Eye')
    axes[1].set_xlabel('Sample Index')
    axes[1].set_ylabel('Sensor Value')
    axes[1].legend()
    axes[1].grid(True)

    plt.tight_layout()
    plt.show()

def fetch_Pandas():
    file_path = 'Data/walking/AFE_000_CONFIDENTIAL.json'
    with open(file_path) as json_file:
        data = json.load(json_file)
        #print(data)
    #convert data to json string
    json_string = json.dumps(data)

    # Extracting eye tracking data and converting it into a pandas dataframe
    eye_data = []

    for entry in data:
        for eye in entry["afe"]:
            if eye and "m" in eye:
                eye_type = eye["t"]
                measurements = eye["m"][0]  # assuming we only need the first set of measurements
                eye_data.append([eye_type] + measurements)

    df = pd.DataFrame(eye_data, columns=["Eye", "Signal1", "Signal2", "Signal3", "Signal4", "Signal5", "Signal6", "Unusable1", "Unusable2"])
    df.head()

    # Plotting the data
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('Eye Tracking Sensor Data')

    # Left Eye (Blue)
    left_eye_data = df[df["Eye"] == "L"]
    for i in range(1, 7):
        axes[(i-1)//3, (i-1)%3].plot(left_eye_data.index, left_eye_data[f'Signal{i}'], color='blue', label=f'Signal{i} (Left Eye)')
        axes[(i-1)//3, (i-1)%3].legend()

    # Right Eye (Green)
    right_eye_data = df[df["Eye"] == "R"]
    for i in range(1, 7):
        axes[(i-1)//3, (i-1)%3].plot(right_eye_data.index, right_eye_data[f'Signal{i}'], color='green', label=f'Signal{i} (Right Eye)')
        axes[(i-1)//3, (i-1)%3].legend()

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
    return df

    # df.head()  # Displa

from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio
import json

app = Flask(__name__)

# Sample Data (Insert your data here)




def create_plots(df):
    fig = px.line(df, x='Index', y='Value', color='Eye', line_group='Signal')
    graphJSON = json.dumps(fig, cls=pio.utils.PlotlyJSONEncoder)
    return graphJSON

@app.route('/')
def home():
    # df = create_dataframe(data)
    df = fetch_Pandas()
    graphJSON = create_plots(df)
    return render_template('index.html', graphJSON=graphJSON)

if __name__ == '__main__':
    app.run(debug=True)