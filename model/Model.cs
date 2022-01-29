public sealed class Model {
    private static Model instance = null;
    private static readonly object instanceLock = new object();
    private List<Entity> ownedEntities;
    private List<Entity> externalEntities;

    private Model () {
        // request player Entity
        ownedEntities = new List<Entity>(/*player*/);
        // fetch external Entity list, and assign it
        externalEntities = new List<Entity>();
    }

    public static Model Instance {
        get {
            lock (instanceLock) {
                if (instance == null) {
                    instance = new Model();
                }
                return instance;
            }
        }
    }

    public List<Entity> Entities {
        get {
            return ownedEntities.Concat(externalEntities).ToList();
        }
    }
}