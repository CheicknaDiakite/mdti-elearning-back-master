# mdti-elearning-back

| Nom      |          champ           | 
|----------|:------------------------:|
| retour 1 |      message, etat       |
| retour 2 | message,  etat,  id/slug |
| retour 3 |  message,  etat, donnee  |

*   Le type des donnée

| Nom        |               champ                | 
|------------|:----------------------------------:|
| etat       |      Boolean  (True / False)       |
| message,id |               string               |
| donnee     | tableau d'objet JSON ou objet JSON |

## Questions

1. [ ] Les images sont envoyés sous quel format ? (avatar, miniature de vidéo)
   * Format base64 Exemple : image = "data:image/png;base64,iVBORw0KGgoAAAA...."
2. [ ] Les documents (CV, et ses diplômes ou attestations) sont envoyés sous quel format ?
   * Format base64 Exemple : doc = "data:application/pdf;base64,sfjdsljfsdlfjslkjfs...."
3. [ ] ...

## Les routes par entité
### Utilisateur

| Action           |             Url              |                                                                                        Paramètre | Retour   |
|------------------|:----------------------------:|-------------------------------------------------------------------------------------------------:|----------|
| connexion        |    utilisateur/connexion     |                                                                               username, password | retour 2 |
| inscription      |   utilisateur/inscription    |                       username, password, first_name, <br/>last_name, email , numero,type_compte | retour 2 |
| get Profil       | utilisateur/profile/get/{id} |                                                                                                  | retour 3 |
| modif. de profil |   utilisateur/profile/set    | utilisateur_id puis le ou les champs à modifier; (new_password et old_password) pour le password | retour 1 |
| recuperation     |       utilisateur/get        |                                                                            [ all, type_compte  ] | retour 3 |

* la photo de profil est **avatar**
*  type de compte : ("admin", "Admin"),
        ("apprenant", "Apprenant"),
        ("instructeur", "Instructeur"),
* genre : ("Homme","Homme"),
        ("Femme","Femme"),

### Categorie (de formation)

| Action      |                Url                 |                              Paramètre | Retour   |
|-------------|:----------------------------------:|---------------------------------------:|----------|
| ajouter     |      formation/categorie/add       |                             nom, image | retour 2 |
| supprimer   |      formation/categorie/del       |                             slug ou id | retour 1 |
| recup. tous |      formation/categorie/get       |                                    --- | retour 3 |
| recup. un   |    formation/categorie/get/{id}    |                                    --- | retour 3 |
| modifier    |      formation/categorie/set       | id ou slug <br/> + (nom et / ou image) | retour 1 |


### SousCategorie (de formation)

| Action      |                Url                |                                          Paramètre | Retour   |
|-------------|:---------------------------------:|---------------------------------------------------:|----------|
| ajouter     |   formation/sous-categorie/add    |                         nom, image, categorie_slug | retour 2 |
| supprimer   |   formation/sous-categorie/del    |                                         slug ou id | retour 1 |
| recup. tous |   formation/sous-categorie/get    |                              categorie_slug ou --- | retour 3 |
| recup. un   | formation/sous-categorie/get/{id} |                              categorie_slug ou --- | retour 3 |
| modifier    |   formation/sous-categorie/set    | id ou slug <br/> , [ nom / image / categorie_slug] | retour 1 |


### Formation

| Action       |         Url          |                                                                                                                                                                     Paramètre | Retour    |
|--------------|:--------------------:|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|-----------|
| ajouter      |    formation/add     |                                                                                                        nom, miniature, prix, sous_categorie_slug, instructeur_id, nombre_heur | retour 2  |
| recuperation |    formation/get     |                                                                                       [publier, moderer, ajout_terminer,  sous_categorie_slug , instructeur_id, apprenant_id] | retour 3  |
| recup. tous  |  formation/get-all   |                                                                                                                                                                               | retour 3  |
| detaille     | formation/get/{slug} |                                                                                                                                                                          slug | retour 3  |
| modification |    formation/set     |  slug, [nom, miniature, prix, sous_categorie_slug, instructeur_id, nombre_heur, description, prerequis, profile_destine, objectif_du_cours, publier, moderer, ajout_terminer] | retour 1  |
| supprimer    |    formation/del     |                                                                                                                                                                    [slug, id] | retour 1  |

*   la suppression sera impossible si la formation à ete une fois acheter au moins

### Chapitre (formation)

| Action       |             Url             |           Paramètre | Retour   |
|--------------|:---------------------------:|--------------------:|----------|
| ajouter      |   formation/chapitre/add    | nom, formation_slug | retour 2 |
| recuperation |   formation/chapitre/get    |      formation_slug | retour 3 |
| recup. tous  | formation/chapitre/get-all  |                     | retour 3 |
| recup . un   | formation/chapitre/get/{id} |      formation_slug | retour 3 |
| modification |   formation/chapitre/set    |           id, [nom] | retour 1 |
| supprimer    |   formation/chapitre/set    |                  id | retour 1 |


### Discution

| Action       |           Url           |                                                   Paramètre | Retour   |
|--------------|:-----------------------:|------------------------------------------------------------:|----------|
| ajouter      | formation/discution/add |  apprenant_id, formation_slug, messageenvoyer_par_apprenant | retour 2 |
| recuperation | formation/discution/get |                                apprenant_id, formation_slug | retour 3 |
| suppression  | formation/discution/del |                                                          id | retour 1 |
| modification | formation/discution/set |                                                   id, [lue] | retour 1 |

* envoyer_par_apprenant : boolean (pour savoir si le message sera afficher a gauche ou a droit)


### Temoignages


| Action       |               Url                |                                     Paramètre | Retour   |
|--------------|:--------------------------------:|----------------------------------------------:|----------|
| ajouter      |    formation/temoignages/add     |         apprenant_id, formation_slug, message | retour 2 |
| recuperation |    formation/temoignages/get     | actif,moderer, [apprenant_id, formation_slug] | retour 3 |
| recuperation | formation/temoignages/get/sans-m |                [apprenant_id, formation_slug] | retour 3 |
| modification |    formation/temoignages/set     |            id, [message,vue ,moderer, actif ] | retour 1 |
| suppression  |    formation/temoignages/del     |                                            id | retour 1 |


### Seance de travail

| Action       |                    Url                    |                                                                                                                        Paramètre | Retour   |
|--------------|:-----------------------------------------:|---------------------------------------------------------------------------------------------------------------------------------:|----------|
| ajouter      |        formation/seancetravail/add        |    apprenant_id, formation_slug, nom,lien_de_la_reunion,date_de_la_reunion, [confirmer_par_instructeur, confirmer_par_apprenant] | retour 2 |
| modifier     |        formation/seancetravail/set        | id, [apprenant_id, formation_slug, nom,lien_de_la_reusion,date_de_la_reunion,confirmer_par_apprenant,confirmer_par_instructeur ] | retour 1 |
| supprimer    |        formation/seancetravail/del        |                                                                                                                                  | retour 1 |
| recuperation |        formation/seancetravail/get        |                                                                                                    apprenant_id,  formation_slug | retour 3 |
| detaille     | formation/seancetravail/get-detaille/{id} |                                                                                                                                  | retour 3 |
| recup. tous  |      formation/seancetravail/get-all      |                                                                                                                                  | retour 3 |


### Cour

| Action           |            Url            |                                Paramètre | Retour   |
|------------------|:-------------------------:|-----------------------------------------:|----------|
| ajouter          |    formation/cour/add     |  apprenant_id, formation_slug, [montant] | retour 2 | 
| modifier         |    formation/cour/set     |      id, [montant,progression,terminer ] | retour 1 | 
| recuperer        |    formation/cour/get     | [apprenant_id,formation_slug, terminer ] | retour 3 | 
| suppresion       |    formation/cour/del     |                                       id | retour 1 | 

*   montant n'est pas obligatoire
*   Si le **montant** n'est pas donner c'est le prix actuel de la formation qui sera pise en charge


### VideoVue

| Action     |           Url           |         Paramètre | Retour   |
|------------|:-----------------------:|------------------:|----------|
| ajouter    | formation/video-vue/add | video_id, cour_id | retour 2 | 
| recuperer  | formation/video-vue/get |           cour_id | retour 3 | 
| suppresion | formation/video-vue/del |           cour_id | retour 1 |


### Video

| Action       |                Url                |                          Paramètre | Retour   |
|--------------|:---------------------------------:|-----------------------------------:|----------|
| ajouter      | formation/video/add/{chapitre_id} |  nom,duree,video,ordre,chapitre_id | retour 2 | 
| recuperer    |        formation/video/get        |                        chapitre_id | retour 3 | 
| modification |        formation/video/set        |  id [nom, duree,ordre,chapitre_id] | retour 1 | 
| suppression  |        formation/video/del        |                                 id | retour 1 | 


### Qcm

| Action        |              Url              |                               Paramètre | Retour   |
|---------------|:-----------------------------:|----------------------------------------:|----------|
| ajouter       |       formation/qcm/add       | nom, description, duree, formation_slug | retour 2 |
| supprimer     |       formation/qcm/del       |                                      id | retour 1 |
| modification  |       formation/qcm/set       |            id [nom, description, duree] | retour 1 |
| recup. tous   |     formation/qcm/get-all     |                                      id | retour 3 |
| recup.        |       formation/qcm/get       |                          formation_slug | retour 3 |
| recup. detail | formation/qcm/get-detail/{id} |                                         | retour 3 |


### Question

| Action       |            Url             |               Paramètre | Retour   |
|--------------|:--------------------------:|------------------------:|----------|
| ajouter      | formation/qcm/question/add | question, qcm_id, point | retour 2 |
| supprimer    | formation/qcm/question/del |                      id | retour 1 |
| modifier     | formation/qcm/question/set |    id, [question,point] | retour 1 |
| recuperation | formation/qcm/question/get |               qcm_id    | retour 3 |


### Reponse

| Action       |              Url               |                     Paramètre | Retour   |
|--------------|:------------------------------:|------------------------------:|----------|
| ajouter      |   formation/qcm/reponse/add    | question_id, reponse,correcte | retour 2 |
| supprimer    |   formation/qcm/reponse/del    |                            id | retour 1 |
| modifier     |   formation/qcm/reponse/set    |        id, [reponse,correcte] | retour 1 |
| recuperation |   formation/qcm/reponse/get    |                   question_id | retour 3 |
| recuperation | formation/qcm/reponse/get/{id} |                               | retour 3 |
| recup. tous  | formation/qcm/reponse/get-all  |                               | retour 3 |


### Examen

| Action        |            Url            |                                  Paramètre | Retour   |
|---------------|:-------------------------:|-------------------------------------------:|----------|
| ajouter       |   formation/examen/add    |       nom,apprenant_id,qcm_id,duree, point | retour 2 |
| modifier      |   formation/examen/set    | id, [nom,apprenant_id,qcm_id,duree, point] | retour 1 |
| supprimer     |   formation/examen/set    |                                         id | retour 1 |
| recuperation  | formation/examen/get/{id} |                                            | retour 3 |
| recup. tous   | formation/examen/get-all  |                                            | retour 3 |
| recuperation  |   formation/examen/get    |                     [apprenant_id, qcm_id] | retour 3 |


### ResultatExamen


| Action      |                Url                 |                         Paramètre | Retour   |
|-------------|:----------------------------------:|----------------------------------:|----------|
| ajouter     |   formation/examen-resultat/add    | examen_id,question_id,response_id | retour 2 |
| supprimer   |   formation/examen-resultat/del    |                                id | retour 1 |
| recup.      |   formation/examen-resultat/get    |                         examen_id | retour 3 |
| recup. un   | formation/examen-resultat/get/{id} |                                   | retour 3 |
| recup. tous | formation/examen-resultat/get-all  |                                   | retour 3 |


### Email

| Action          |    Url    |                  Paramètre | Retour     |
|-----------------|:---------:|---------------------------:|------------|
| envoyer un mail | mail/send |  sujet,message,email_liste | retourn 1  |

*   email_liste : email@email.com ou 
*   email1@email.com,email2@email.com,email3@email.com,....


# ANCIEN SUJET

### Type (examen, concour, ...)

| Action       |            Url             | Paramètre | Retour    |
|--------------|:--------------------------:|----------:|-----------|
| ajouter      |   ancien-sujet/type/add    |       nom | retourn 1 |
| recuper tout |   ancien-sujet/type/get    |           | retourn 3 |
| recuper un   | ancien-sujet/type/get/{id} |           | retourn 3 |
| supprimer    |   ancien-sujet/type/del    |        id | retourn 2 |


### Niveau

| Action       |             Url              | Paramètre | Retour    |
|--------------|:----------------------------:|----------:|-----------|
| ajouter      |   ancien-sujet/niveau/add    |       nom | retourn 1 |
| recuper tout |   ancien-sujet/niveau/get    |           | retourn 3 |
| recuper un   | ancien-sujet/niveau/get/{id} |           | retourn 3 |
| supprimer    |   ancien-sujet/niveau/add    |        id | retourn 2 |



### Matiere

| Action       |              Url              | Paramètre | Retour    |
|--------------|:-----------------------------:|----------:|-----------|
| ajouter      |   ancien-sujet/matiere/add    |       nom | retourn 1 |
| recuper tout |  ancien-sujet/matiere/get     |           | retourn 3 |
| recuper un   | ancien-sujet/matiere/get/{id} |           | retourn 3 |
| supprimer    |   ancien-sujet/matiere/add    |        id | retourn 2 |



### A venir

| Action | Url | Paramètre | Retour |
|--------|:---:|----------:|--------|
|        |     |           |        |