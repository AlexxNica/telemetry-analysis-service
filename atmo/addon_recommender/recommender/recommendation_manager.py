from collaborative_recommender import CollaborativeRecommender
from empty_recommender import EmptyRecommender
from profile_fetcher import ProfileFetcher


class RecommendationManager:
    """
    """
    info_fetcher = None
    recommenders = []

    def __init__(self):
        # Instantiate the object to get the client info.
        if RecommendationManager.info_fetcher is None:
            RecommendationManager.info_fetcher = ProfileFetcher()

        # Init the recommenders. Note: ORDER MATTERS!
        # The recommendation logic will go through each recommender and pick the
        # first one that "can_recommend".
        if not RecommendationManager.recommenders:
            RecommendationManager.recommenders.append(CollaborativeRecommender())
            RecommendationManager.recommenders.append(EmptyRecommender())

    def recommend(self, client_id, limit):
        # Get the info for the requested client id.
        client_info = RecommendationManager.info_fetcher.get(client_id)

        # Compute the recommendation.
        suggestions = None
        for r in RecommendationManager.recommenders:
            if r.can_recommend(client_info):
                return r.recommend(client_info, limit)
