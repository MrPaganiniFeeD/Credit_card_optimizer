import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

class RecommendSystem:

    card_sim_df = pd.DataFrame()

    def __init__(self, transaction_df):
        self.transaction_df = transaction_df
        self.card_sim_df = self.calculate_cosine(self.transaction_df)

    def calculate_cosine(self, data):
        df = data
        card_features = df.groupby("Card ID").agg({
            'Скидка на категорию': 'mean',
            'Проценты по кредиту': 'mean',
            'Кэшбек на категорию': 'mean',
            'rating': 'mean',
            'Категория': 'first'
        }).reset_index()

        card_features = pd.get_dummies(card_features, columns=['Категория'])

        features = card_features.drop(columns=['Card ID'])

        scaler = StandardScaler()
        feature_matrix = scaler.fit_transform(features)

        similarity_matrix = cosine_similarity(feature_matrix)

        card_sim_df = pd.DataFrame(similarity_matrix, index=card_features['Card ID'], columns=card_features['Card ID'])
        return card_sim_df
        
    def get_recommend_cards(self, user_id: int, top_n=1) -> list:
        df = self.transaction_df
        user_cards = df[df['User ID'] == user_id]['Card ID'].unique()
        similarity_scores = self.card_sim_df[user_cards].mean(axis=1)
        recommendations = similarity_scores.sort_values(ascending=False).head(top_n)

        return list(recommendations.index)

data = {
    'User ID': [1, 1, 2, 2, 3, 3],
    'Card ID': [101, 102, 101, 103, 102, 103],
    'Категория': ['groceries', 'dining', 'groceries', 'travel', 'dining', 'travel'],
    'Скидка на категорию': [0.05, 0.03, 0.04, 0.06, 0.02, 0.05],
    'Проценты по кредиту': [0.15, 0.12, 0.14, 0.16, 0.13, 0.15],
    'Кэшбек на категорию': [0.02, 0.03, 0.01, 0.04, 0.02, 0.03],
    'rating': [5, 4, 3, 5, 2, 4]
}

rec = RecommendSystem(pd.DataFrame(data))

user_id = 1
recommended = rec.get_recommend_cards(user_id)
print(f"Рекомендуемые карты для пользователя {user_id}: {recommended}")
