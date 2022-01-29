public sealed class Model {
    private static Model instance = null;
    private static readonly object instanceLock = new object();
    private List<Entity> ownedEntities;

    private Model () {
        // request player Entity
        ownedEntities = new List<Entity>(/*player*/);
        // fetch external Entity list
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
}