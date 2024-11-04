def calculate_acceptance_ratio(successful_embeddings, total_requests):
    if total_requests == 0:
        return 0
    return successful_embeddings / total_requests

def calculate_revenue_to_cost_ratio(revenue, cost):
    if cost == 0:
        return revenue  # Return revenue if cost is zero to avoid division by zero
    return revenue / cost