// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

public sealed class Model {
    private static Model instance = null;
    private static readonly object instanceLock = new object();

    private Model () {}

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