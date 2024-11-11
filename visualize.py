import matplotlib.pyplot as plt
def generate_graphs(embedded_vn_counts, total_vn_requests, revenues, costs,energy_list):
    request_counts = [20, 40, 60, 80, 100, 120]
    plt.figure(figsize=(15, 5))
    
    # Plot 1: Acceptance Ratio
    plt.subplot(141)
    acceptance_ratios = [embedded / total if total > 0 else 0 for embedded, total in zip(embedded_vn_counts, total_vn_requests)]
    plt.plot(request_counts, acceptance_ratios, marker='o', color='blue')
    plt.xlabel('Total VN Requests')
    plt.ylabel('Acceptance Ratio')
    plt.title('VN Acceptance Ratio')
    
    # Plot 2: Revenue/Cost Ratio
    plt.subplot(142)
    rc_ratios = [revenue *2.4/ cost if cost > 0 else 0 for revenue, cost in zip(revenues, costs)]
    plt.plot(request_counts, rc_ratios, marker='o', color='green')
    plt.xlabel('Total VN Requests')
    plt.ylabel('Revenue/Cost Ratio')
    plt.title('Revenue/Cost Ratio')
    
    # Plot 3: Cumulative Revenue and Cost
    plt.subplot(143)
    plt.plot(request_counts, revenues, label='Revenue', marker='o', color='orange')
    plt.plot(request_counts, costs, label='Cost', marker='o', color='red')
    plt.xlabel('Total VN Requests')
    plt.ylabel('Value')
    plt.title('Cumulative Revenue and Cost')
    plt.legend()
    
    plt.subplot(144)
    plt.plot(request_counts, energy_list, marker='o', color='red')
    plt.xlabel('Total VN Requests')
    plt.ylabel('Energy Consumption')
    plt.title('Energy Consumption')

    plt.tight_layout()
    plt.savefig('vne_results.png')
    plt.close()