"""Starter Plotly Dash app for SpaceX landing prediction.
Run after notebooks/03_data_wrangling.ipynb creates data/processed/spacex_falcon9_launches.csv.
From the project root: python dashboard/app.py
"""
from pathlib import Path
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "processed" / "spacex_falcon9_launches.csv"
if not DATA_PATH.exists():
    raise FileNotFoundError(f"{DATA_PATH} not found. Run notebook 03_data_wrangling.ipynb first.")
df = pd.read_csv(DATA_PATH)
df["landing_attempt"] = df["landing_attempt"].astype(str).str.lower().eq("true")
df["landing_success"] = pd.to_numeric(df["landing_success"], errors="coerce")
df["Class"] = df["landing_success"]
sites = sorted(df["launch_site"].dropna().unique())
app = Dash(__name__)
app.title = "SpaceX Falcon 9 Landing Analytics"

app.layout = html.Div([
    html.H1("SpaceX Falcon 9 First-Stage Landing Analytics"),
    html.P("Explore historical launches. Charts use the locally generated API snapshot."),
    html.Label("Launch site"),
    dcc.Dropdown(id="site", options=[{"label":"All sites","value":"ALL"}] +
                 [{"label":s,"value":s} for s in sites], value="ALL", clearable=False),
    dcc.Graph(id="outcomes"),
    dcc.Graph(id="payload"),
    html.Div(id="summary")
], style={"maxWidth":"1100px","margin":"auto","fontFamily":"Arial"})

@app.callback(
    Output("outcomes","figure"), Output("payload","figure"), Output("summary","children"),
    Input("site","value")
)
def update(site):
    d = df.copy() if site == "ALL" else df[df["launch_site"] == site].copy()
    landing = d[d["landing_attempt"] & d["landing_success"].notna()]
    if landing.empty:
        pie = px.pie(names=["No labelled landing attempts"], values=[1], title="Landing outcomes")
    else:
        counts = landing["landing_success"].map({True:"Successful landing",False:"Unsuccessful landing"}).value_counts().reset_index()
        counts.columns = ["Outcome","Count"]
        pie = px.pie(counts, names="Outcome", values="Count", title="First-Stage Landing Outcomes")
    scatter_data = d[d["landing_attempt"] & d["landing_success"].notna()].copy()
    scatter_data["Outcome"] = scatter_data["landing_success"].map({1.0:"Successful",0.0:"Unsuccessful"})
    scatter = px.scatter(scatter_data, x="payload_mass_kg", y="flight_number",
                         color="Outcome", hover_data=["mission_name","launch_site","year"],
                         title="Payload Mass vs Flight Number by Landing Outcome",
                         labels={"payload_mass_kg":"Payload mass (kg)","flight_number":"Flight number"})
    rate = (100 * landing["landing_success"].mean()) if not landing.empty else float("nan")
    summary = f"Launch records: {len(d)} | Labelled landing attempts: {len(landing)} | Landing success rate: {rate:.1f}%" if landing.shape[0] else f"Launch records: {len(d)} | No labelled landing attempts in this selection."
    return pie, scatter, summary

if __name__ == "__main__":
    app.run(debug=False)
