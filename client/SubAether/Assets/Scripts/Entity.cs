using System.Collections;
using System.Collections.Generic;
using UnityEngine;

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
    public Vector2 Position { get; set; }
    public EntityType Type { get; }

    public Entity (
        int identity, 
        bool aetherStatus, 
        bool destroyStatus,
        Vector2 position,
        EntityType type) {
            Identity = identity;
            AetherStatus = aetherStatus;
            DestroyStatus = destroyStatus;
            Position = position;
            Type = type;
        }
}
