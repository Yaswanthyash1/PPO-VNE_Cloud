# PPO-VNE: Proximal Policy Optimization for Virtual Network Embedding

## Overview

The PPO-VNE framework offers a novel approach to solving the Virtual Network Embedding (VNE) problem by leveraging deep reinforcement learning techniques, specifically the Proximal Policy Optimization (PPO) algorithm. This framework aims to optimize resource utilization and minimize energy consumption while dynamically mapping virtual network requests to substrate networks.

## Features

- **Deep Reinforcement Learning**: Utilizes the PPO algorithm for efficient policy optimization in dynamic network environments.
- **Hybrid Feature Extraction**: Combines manually engineered features with Graph Convolutional Network (GCN) derived features to enhance decision-making capabilities.
- **Multi-Objective Optimization**: Balances competing objectives such as acceptance rate, revenue generation, and energy efficiency.
- **Simulation Environment**: Mimics real-world network conditions to facilitate thorough evaluation and testing.

## Methodology

The methodology includes:

1. **Reinforcement Learning Framework**:
   - **State Representation**: Considers the substrate network status and details of virtual network requests.
   - **Actions**: Defined for making embedding decisions.
   - **Rewards**: Guide the RL agent towards optimal embedding strategies.

2. **Hybrid Feature Extraction**:
   - Integrates basic network metrics with GCN-derived features for comprehensive analysis.

3. **Multi-Objective Optimization**:
   - Implements a custom reward function to balance acceptance rates, revenue, and energy efficiency.

4. **Policy Optimization via PPO**:
   - Ensures stable learning and adaptation to network changes through the use of the PPO algorithm.

## Implementation

The PPO-VNE framework has been implemented in a simulated network environment with the following specifications:

- **Substrate Network**: 100 nodes and approximately 500 links.
- **Traffic Generation**: Virtual network requests are generated based on a Poisson process to simulate realistic traffic conditions.

### Requirements

To run the PPO-VNE framework, ensure you have the following:

- **Python Version**: 3.x
- **Required Libraries**:
  - NumPy
  - TensorFlow or PyTorch
  - NetworkX
  - Matplotlib (for visualization)

### Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/PPO-VNE.git
   cd PPO-VNE
   
2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   
### Usage

1. To run the PPO-VNE framework, execute the main script:
     ```bash
       python main.py

  You can modify the parameters in config.py to adjust the simulation settings, such as the number of nodes, link creation probability, and VNR arrival rates.

## Results

The framework has demonstrated superior performance in key metrics compared to baseline VNE approaches, including:

- Higher acceptance rates
- Increased overall revenue
- Improved revenue-to-cost and revenue-to-energy ratios.


![WhatsApp Image 2024-11-11 at 19 22 08_364cda33](https://github.com/user-attachments/assets/704a526e-161d-4a5d-8ce8-3c1e083ee802)



For detailed results and analyses, please refer to the Results and Analysis section in the report.

## Future Work

Future enhancements for the PPO-VNE framework may include:

- Exploring advanced multi-objective optimization techniques.
- Extending the framework to applications in emerging fields such as IoT and cloud-based networks.

## Contact

For questions or inquiries, please contact:

<div style="font-family: Arial, sans-serif; font-size: 16px;">
  <strong>N Yaswanth</strong> <br>
  <a href="mailto:your.email@example.com">yaswanthnamburi1010@gmail.com</a>
   
   <strong>Syed Farhan</strong> <br>
  <a href="mailto:your.email@example.com">syedfarhan.221cs254@nitk.edu.in</a>
  
   <strong>Vishruth S Kumar</strong> <br>
  <a href="mailto:your.email@example.com">vishruthskumar.221cs262@nitk.edu.in</a>
  
   <strong>Yashas</strong> <br>
  <a href="mailto:your.email@example.com">yashas.221cs265@nitk.edu.in</a>
</div>
