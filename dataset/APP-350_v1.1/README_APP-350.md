# APP-350 Corpus

The APP-350 Corpus consists of 350 annotated Android app privacy policies.

The dataset is made available for research, teaching, and scholarship purposes only, with further parameters in the spirit of a Creative Commons Attribution-NonCommercial License. Contact Prof. Norman Sadeh with any questions.

If you use this dataset as part of a publication, you must cite the following paper:

> MAPS: Scaling Privacy Compliance Analysis to a Million Apps. Sebastian Zimmeck, Peter Story, Daniel Smullen, Abhilasha Ravichander, Ziqi Wang, Joel Reidenberg, N. Cameron Russell, and Norman Sadeh. Privacy Enhancing Technologies Symposium 2019.


## File Format

The HTML of each privacy policy is saved in the `original_documents` subdirectory. However, it is not necessary to use these documents. Instead, you can simply read the annotated documents from the `annotations` subdirectory. Each file in the `annotations` subdirectory has the following format:

```yaml
policy_id: 1
policy_name: 6677G
policy_type: TEST
segments:
- segment_id: 11
  segment_text: '... our products. When you register with us, you provide us
    with certain personal information, such as a username, date and month of
    birth, and your email address. The information you disclose ...'
  annotations:
    - modality: PERFORMED
      practice: Demographic_Age_1stParty
    - modality: PERFORMED
      practice: Contact_E_Mail_Address_1stParty
  sentences:
  - annotations:
    - modality: PERFORMED
      practice: Demographic_Age_1stParty
    - modality: PERFORMED
      practice: Contact_E_Mail_Address_1stParty
    sentence_text: When you register with us, you provide us with certain
      personal information, such as a username, date and month of birth, and
      your email address.
```

Each policy has one or more segments, some of which are annotated. Segments are structurally related parts of policy text that loosely correspond to paragraphs. If the segment is annotated, the specific sentences which were annotated are also described. It is assumed that unannotated segments neither affirm nor deny the performance of practices, and so can be used as negative training examples.


## Annotation Scheme

Each annotation consists of a practice and a modality.

A *privacy practice* (or *practice*) describes a certain behavior of an app that can have privacy implications (e.g., collection of a phone's device identifier or sharing of its location with ad networks). We have annotations for 58 different practices. Each of the data types listed below (except for SSO and Facebook_SSO) appears in the dataset as both 1stParty and 3rdParty practices. The SSO and Facebook_SSO data types appear directly as practices, because all data is exchanged between the app developer as first party and the SSO provider as third party.

There are only two modalities: PERFORMED  (i.e., a practice is explicitly described as being performed) and NOT_PERFORMED (i.e., a practice is explicitly described as not being performed).

| Data Type                         | Description |
| --------------------------------- | ----------- |
| Contact                           | The policy describes collection of unspecified contact data. |
| Contact_Address_Book              | The policy describes collection of contact data from a user's address book on the phone. |
| Contact_City                      | The policy describes collection of the user's city. |
| Contact_E_Mail_Address            | The policy describes collection of the user's e-mail. |
| Contact_Password                  | The policy describes collection of the user's password. |
| Contact_Phone_Number              | The policy describes collection of the user's phone number. |
| Contact_Postal_Address            | The policy describes collection of the user's postal address. |
| Contact_ZIP                       | The policy describes collection of the user's ZIP code. |
| Demographic                       | The policy describes collection of the user's unspecified demographic data. |
| Demographic_Age                   | The policy describes collection of the user's age (including birth date and age range). |
| Demographic_Gender                | The policy describes collection of the user's gender. |
| Identifier                        | The policy describes collection of the user's unspecified identifiers. |
| Identifier_Ad_ID                  | The policy describes collection of the user's ad ID (such as the Google Ad ID). |
| Identifier_Cookie_or_similar_Tech | The policy describes collection of the user's HTTP cookies, flash cookies, pixel tags, or similar identifiers. |
| Identifier_Device_ID              | The policy describes collection of the user's device ID (such as the Android ID). |
| Identifier_IMEI                   | The policy describes collection of the user's IMEI (International Mobile Equipment Identity). |
| Identifier_IMSI                   | The policy describes collection of the user's IMSI (International Mobile Subscriber Identity). |
| Identifier_IP_Address             | The policy describes collection of the user's IP address. |
| Identifier_MAC                    | The policy describes collection of the user's MAC address. |
| Identifier_Mobile_Carrier         | The policy describes collection of the user's mobile carrier name or other mobile carrier identifier. |
| Identifier_SIM_Serial             | The policy describes collection of the user's SIM serial number. |
| Identifier_SSID_BSSID             | The policy describes collection of the user's SSID or BSSID. |
| Location                          | The policy describes collection of the user's unspecified location data. |
| Location_Bluetooth                | The policy describes collection of the user's Bluetooth location data. |
| Location_Cell_Tower               | The policy describes collection of the user's cell tower location data. |
| Location_GPS                      | The policy describes collection of the user's GPS location data. |
| Location_IP_Address               | The policy describes collection of the user's IP location data. |
| Location_WiFi                     | The policy describes collection of the user's WiFi location data. |
| SSO                               | The policy describes receiving data from an unspecified single sign on service. |
| Facebook_SSO                      | The policy describes receiving data from the Facebook single sign on service. |

| Party    | Description |
| -------- | ----------- |
| 1stParty | The policy describes collection of data from the user by the app publisher. |
| 3rdParty | The policy describes collection of data from the user by ad networks, analytics services, or other third parties. |
