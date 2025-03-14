import pandas as pd
import numpy as np

def align_agents_transforms_on_time(agents_list, transforms_dict):
    """
    Align both agents and transforms data on a unified set of timestamps.
    
    Args:
        agents_list: List of DataFrames, each with a "time" column.
        transforms_dict: Dictionary where each value is a DataFrame with a "time" column.
    
    Returns:
        aligned_agents: List of aligned agent DataFrames.
        aligned_transforms: Dictionary of aligned transform DataFrames.
    """
    # Get unique timestamps from agents
    if agents_list:
        agent_times = pd.concat([df["time"] for df in agents_list]).sort_values().unique()
    else:
        agent_times = np.array([])
    
    # Get unique timestamps from transforms
    if transforms_dict:
        transform_times = pd.concat([df["time"] for df in transforms_dict.values()]).sort_values().unique()
    else:
        transform_times = np.array([])
    
    # Compute the union of timestamps from both sources
    all_times = np.union1d(agent_times, transform_times)
    
    # Align agents: reindex each DataFrame to all_times and fill missing values
    aligned_agents = []
    for agent_df in agents_list:
        agent_df = agent_df.drop_duplicates(subset="time")  # Drop duplicate timestamps
        aligned = agent_df.set_index("time").reindex(all_times)
        aligned = aligned.ffill().bfill().reset_index().rename(columns={"index": "time"})
        aligned = aligned.drop_duplicates(subset="time")  # Drop duplicate timestamps
        aligned_agents.append(aligned)
    
    # Align transforms: reindex each DataFrame similarly
    aligned_transforms = {}
    for key, df in transforms_dict.items():
        df = df.drop_duplicates(subset="time")  # Drop duplicate timestamps
        aligned = df.set_index("time").reindex(all_times)
        aligned = aligned.ffill().bfill().reset_index().rename(columns={"index": "time"})
        aligned = aligned.drop_duplicates(subset="time")  # Drop duplicate timestamps
        aligned_transforms[key] = aligned
    
    return aligned_agents, aligned_transforms

def align_agents_on_time(agents_list):
    """Align agent DataFrames using timestamps."""
    # Collect all unique timestamps across all agents
    all_times = pd.concat([agent["time"] for agent in agents_list]).sort_values().unique()
    
    aligned_agents = []
    for agent_df in agents_list:
        # Set time as index and reindex to all_times
        aligned = agent_df.set_index("time").reindex(all_times)
        # Forward-fill and backward-fill missing values
        aligned = aligned.ffill().bfill().reset_index()
        aligned_agents.append(aligned)
    
    return aligned_agents