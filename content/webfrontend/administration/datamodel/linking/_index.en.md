---
title: "Linking"
menu:
  main:
    name: "Linking"
    identifier: "webfrontend/administration/datamodel/linking"
    parent: "webfrontend/administration/datamodel"
---
# Linking

In easydb there are several ways to link other object types to access other lists, controlled vocabularies or thesauri. These are explained below.



## Forward Link

If you do not want to use text input, but instead want to access other lists, controlled vocabularies or thesauri, you simply select another object type in the data model for this field, whose contents are then available in this field. 

**Example:** you want to access a list of photographers for a photo to avoid having to enter the name of the photographer manually each time.

This is a so-called "forward linking". This means that the photo knows which photographer is linked, but the linked photographer has no information about which photos he is linked to. When exporting photographers, there is no information about the photos to which the photographer is linked. 

In order to display all photos linked to the photographer in the detailed view, the plugin https://github.com/programmfabrik/easydb-custom-mask-splitter-detail-linked-plugin can be used.



## Reverse Edit (Hierarchy)

This option is only available for hierarchical object types and is located on the "General" tab under "Database options". 

**Example:**

    Germany
        Berlin
        	Prenzlauer Berg
        	Mitte
        Hamburg
        Munich
    Spain
        Barcelona
        Lisbon



By default, the entry "Germany" does not know that the entries "Berlin", "Hamburg" and "Munich" are below it. Only "Berlin", "Hamburg" and "Munich" know that they are under "Germany". This means that in the detailed view of "Germany" you do not see the subordinate entries, but only the parent entry for the subordinate entries.

If you want to be able to see and possibly even edit the directly subordinate entries for "Germany", you have to activate "Reverse Edit" for the object type. Afterwards an automatically generated line is available in the mask over which one can control, which information of the subordinate entries is to be indicated and/or be able to be edited. In the input mask there is also a plus available to be able to create new subordinate entries. 

The information of the subordinate entries is integrated into the index of the parent entry and is thus also available in the search and export.



## Reverse Edit (Simple)

"Reverse Edit" is used when you want to link two different object types and integrate the information of one of these object types into the other. As an example, we can use the linking of collection objects and photos. Let's assume that a photo should only ever be linked to one collection object and that a collection object can have several photos. Without "Reverse Edit", one would insert a multiple field with linking to the object type "Photos" in the object type "Collection objects". However, this would mean that it would not be possible to see which collection object the photos are linked to. If you were to include the link on pages of the "Photos" object type, you would not see the photos in the collection objects. 

To make this possible, a simple link field to the object type "Collection objects" must be installed in the object type "Photos" and "Reverse Edit" must be activated there. This causes the information of the photos to be integrated into the "Collection objects" object type. In the collection object mask, a line is automatically created for the photos, which can be used to control which fields can be viewed or directly edited from the collection object. It is also possible to create new photos from the collection object and link them directly to the collection object. 

The information of the included object types is indexed and is available in the search in the export (in this case, when exporting collection objects, information on the photos is also included).



## Reverse Edit (Double)

If you want to connect two different object types in such a way that a multiple link can be viewed or edited on both sides, you must create a so-called connection object type that contains two fields. This may be necessary, for example, in the case of loans. Let's say we have an object type "Collection objects" and an object type "Loans", we want to be able to see and edit which collection objects have been loaned in the loans record and to see and edit which loan transactions are linked in collection objects.

**Example object type "Collection object loans":**

| Field Name        | Data Type                                | Reverse Edit |
| ----------------- | ---------------------------------------- | ------------ |
| Collection Object | Link to object type "Collection Objects" | Ja           |
| Loan              | Link to object type "Loans"              | Ja           |



By activating "Reverse" for both fields, a line is generated in the masks of the object types used there, which can be used to control, among other things, whether the link can only be viewed or also edited. 

If you edit a loan and add a collection object to it, the collection object is automatically linked to the loan. The information is integrated into the index of both object types and is thus also available in the search and export.



## Bidirectional

The bidirectional link is only available in the object type when linking to the same object type in a multiple field.

**Example:** you want to link from one collection object to another collection object to record relationships / references between different collection objects.

By default, when linking from object A to object B, only a link from A to B is saved. This means that object B does not know that object A refers to it. You would therefore also have to edit object B and manually store a link to object A. Since this is not manageable especially with large amounts of data and also error-prone, this can be automated by activating "bidirectional" for the field. This has the effect that when object A is linked to object B, a so-called backlink to object A is automatically saved for object B. This means that the link can be created on both sides. This means that the link can be viewed and edited on both sides and is constantly kept synchronized. If there are several fields in the multiple field, such as a comment, these are also saved on both sides.



## Bidirectional Reverse

"Bidirectional Reverse" only makes sense in the context of a bidirectional link. If we take the example from the bidirectional linking again (see above), it may be that this linking of object A and object B should also be given an attribute. For example, what type of relationship it is. If we assume that object B is a part of object A, this means that object A consists of the part object B. So if now this link between object A and B would be created automatically via bidirectional linking, the attribute "is part of" would be on both pages. This would be wrong, of course. This is where "bidirectional reverse" comes into play. 

In the object type used for the attribute (in our example "Reference Type"), it must be specified which attribute pairs belong together. In our case, this would be the entries "is part of" and "has parts". 



**Example object type "Reference type":**

| Field Name                | Data Typ                             | Bidirektional Reverse | Comment                                                      |
| ------------------------- | ------------------------------------ | --------------------- | ------------------------------------------------------------ |
| Reference type            | Free Text                            |                       | Name of the reference type, e.g. "is part of".               |
| Associated reference type | Link to object type "Reference type" | Yes                   | the reference type to be used in the so-called reverse link, e.g. "has parts of". |



**Entries "Reference type":**

| Reference Type | Associated Reference Type |
| -------------- | ------------------------- |
| is part of     | hat Teile                 |
| has parts      | has parts                 |



If the link type "is part of" is selected in a bidirectional link, the link type "has parts" is automatically set when the so-called backlink is saved.
