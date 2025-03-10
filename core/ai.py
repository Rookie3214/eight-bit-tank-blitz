# core/utils/ai.py

class EnemyAI:
    """
    Simple placeholder for enemy AI logic.
    In a more complete game, this would patrol or defend.
    """
    def __init__(self, tank):
        self.tank = tank

    def update(self, dt):
        # Placeholder logic: do nothing
        pass


class AllyAI:
    """
    Simple placeholder for allied AI logic.
    Could follow the player or move to waypoints.
    """
    def __init__(self, tank):
        self.tank = tank

    def update(self, dt):
        # Placeholder logic: do nothing
        pass
