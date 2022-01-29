public enum EntityType {
    Player,
    Torpedo,
    Mine,
    Environment
}

public class Entity {
    public int Identity { get; }
    public bool AetherStatus { get; set; }
    public bool DestroyStatus { get; set; }
    public (int, int) Position { get; set; }
    public EntityType Type { get; }

    public Entity (
        int identity, 
        bool aetherStatus, 
        bool destroyStatus,
        (int, int) position,
        EntityType type) {
            Identity = identity;
            AetherStatus = aetherStatus;
            DestroyStatus = destroyStatus;
            Position = position;
            Type = type;
        }
}