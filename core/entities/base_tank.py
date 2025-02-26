class BaseTank:
    def __init__(self, name, damage, health, speed, maneuverability, hitbox):
        self.name = name
        self.damage = damage
        self.health = health
        self.speed = speed
        self.maneuverability = maneuverability
        self.hitbox = hitbox  # Could be a pygame.Rect or similar structure

    def move(self, direction):
        # Implement movement logic (forward, reverse, left, right)
        pass

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.destroy()

    def destroy(self):
        # Handle tank destruction
        pass