// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

public enum GameObjectType {
    Player,
    Torpedo,
    Mine,
    Environment
}

public class GameObject {
    public int Identity { get; }
    public bool AetherStatus { get; set; }
    public bool DestroyStatus { get; set; }
    public (int, int) Position { get; set; }
    public GameObjectType Type { get; }

    public GameObject (
        int identity, 
        bool aetherStatus, 
        bool destroyStatus,
        (int, int) position,
        GameObjectType type) {
            Identity = identity;
            AetherStatus = aetherStatus;
            DestroyStatus = destroyStatus;
            Position = position;
            Type = type;
        }
}

public sealed class Model {
    private static Model instance = null;
    private static readonly object instanceLock = new object();
    private List<GameObject> ownedObjects;

    private Model () {
        // request player gameObject
        ownedObjects = new List<GameObject>(/*player*/);
        // fetch external gameObject list
    }

    private static Model Instance {
        get {
            lock (instanceLock) {
                if (instance == null) {
                    instance = new Model();
                }
                return instance;
            }
        }
    }
}