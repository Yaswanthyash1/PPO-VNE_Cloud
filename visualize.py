# visualize.py
import matplotlib.pyplot as plt

def generate_graphs(embedded_vn_counts, total_vn_requests, revenues, costs):
    plt.figure(figsize=(15, 5))
    
    # Use only the final data point
    final_vn_requests = total_vn_requests[-1]
    final_embedded = embedded_vn_counts[-1]
    final_revenue = revenues[-1]
    final_cost = costs[-1]
    
    # Plot 1: Acceptance Ratio
    plt.subplot(131)
    acceptance_ratio = final_embedded / final_vn_requests if final_vn_requests > 0 else 0
    plt.scatter(final_vn_requests, acceptance_ratio, color='blue', s=100)
    plt.xlabel('Total VN Requests')
    plt.ylabel('Acceptance Ratio')
    plt.title('Final VN Acceptance Ratio')
    
    # Plot 2: Revenue/Cost Ratio
    plt.subplot(132)
    rc_ratio = final_revenue / final_cost if final_cost > 0 else 0
    plt.scatter(final_vn_requests, rc_ratio, color='green', s=100)
    plt.xlabel('Total VN Requests')
    plt.ylabel('Revenue/Cost Ratio')
    plt.title('Final Revenue/Cost Ratio')
    
    # Plot 3: Cumulative Revenue and Cost
    plt.subplot(133)
    plt.scatter(final_vn_requests, final_revenue, label='Revenue', color='orange', s=100)
    plt.scatter(final_vn_requests, final_cost, label='Cost', color='red', s=100)
    plt.xlabel('Total VN Requests')
    plt.ylabel('Value')
    plt.title('Final Cumulative Revenue and Cost')
    plt.legend()
    
    plt.tight_layout()
    plt.savefig('vne_results.png')
    plt.close()
