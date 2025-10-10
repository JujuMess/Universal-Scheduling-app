#test mismatch check
from app.universal_scheduling_app import check_mismatch
import pandas as pd

# Simulated Team sheet
df_team = pd.DataFrame({
    "agent_name": ["alice_smith", "bob_jones", "carla_martin", "daniel_wong"]
})

# Simulated History sheet
df_history = pd.DataFrame({
    "agent_name": ["alice_smith", "bob_jones", "daniel_wong"]
})

# Simulated Holiday sheet
df_holiday = pd.DataFrame({
    "agent_name": ["alice_smith", "bob_jones", "carla_martin", "emily_ross"]  # emily_ross not in team → mismatch
})

# Simulated Schedule sheet
df_schedule = pd.DataFrame({
    "agent_name": ["alice_smith", "bob_jones", "daniel_wong", "frank_zhou"]   # frank_zhou not in team → mismatch
})


def test_check_mismatch():
    assert check_mismatch(df_team, df_history, df_holiday, df_schedule) == "emily_ross in holiday, frank_zhou in schedule", "missing carla_martin in df_team"