using System.Collections;
using System.Collections.Generic;
using System.Net.Http;
using System.Linq;
using UnityEngine;

    // Update is called once per frame
    // void Update()
    // {
    //
    // }

public sealed class Model : MonoBehaviour {
    private static Model instance = null;
    private static readonly object instanceLock = new object();
    private List<Entity> ownedEntities;
    private List<Entity> externalEntities;
    private static readonly HttpClient client = new HttpClient();
    private static string hostName = "http://lore.mccoshen:5000";

    private async void registerPlayer() {
        HttpResponseMessage response = await client.PostAsync(hostName + "/register", null);
    }

    private IEnumerator registerRoutine() {
        registerPlayer();
        yield return null;
    }

    void Start () {
        // request player Entity
        ownedEntities = new List<Entity>();
        StartCoroutine(registerRoutine());
        // fetch external Entity list, and assign it
        externalEntities = new List<Entity>();
    }

    public List<Entity> Entities {
        get {
            return ownedEntities.Concat(externalEntities).ToList();
        }
    }
}
