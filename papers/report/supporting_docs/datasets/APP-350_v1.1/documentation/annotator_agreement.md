# Annotator Agreement

High inter-annotator agreement signals the reliability of the ground-truth on which classifiers can be trained and tested. We calculated annotator agreement at the level of each privacy policy. Thus, for the purposes of calculating agreement, we do not require annotators to annotate the same spans of text. Instead, we simply require that they include the same sets of annotations anywhere in the policy. Agreement is good above 0.8, fair between 0.67 and 0.8, and doubtful below 0.67 (C. D. Manning, P. Raghavan, and H. Schutze, Introduction to Information Retrieval. Cambridge University Press, 2008).

| Privacy Practice                           | Krippendorf's Alpha |
| ------------------------------------------ | ------------------- |
| Contact_1stParty                           | 0.75                |
| Contact_3rdParty                           | 0.65                |
| Contact_Address_Book_1stParty              | 0.92                |
| Contact_Address_Book_3rdParty              | 0.74                |
| Contact_City_1stParty                      | 0.59                |
| Contact_City_3rdParty                      | 0.59                |
| Contact_E_Mail_Address_1stParty            | 0.7                 |
| Contact_E_Mail_Address_3rdParty            | 0.8                 |
| Contact_Password_1stParty                  | 0.64                |
| Contact_Password_3rdParty                  | -0.01               |
| Contact_Phone_Number_1stParty              | 0.96                |
| Contact_Phone_Number_3rdParty              | 0.92                |
| Contact_Postal_Address_1stParty            | 0.71                |
| Contact_Postal_Address_3rdParty            | 0.83                |
| Contact_ZIP_1stParty                       | 0.88                |
| Contact_ZIP_3rdParty                       | 1                   |
| Demographic_1stParty                       | 0.39                |
| Demographic_3rdParty                       | 0.65                |
| Demographic_Age_1stParty                   | 0.85                |
| Demographic_Age_3rdParty                   | 0.74                |
| Demographic_Gender_1stParty                | 0.91                |
| Demographic_Gender_3rdParty                | 0.74                |
| Identifier_1stParty                        | 0.63                |
| Identifier_3rdParty                        | 0.55                |
| Identifier_Ad_ID_1stParty                  | 0.89                |
| Identifier_Ad_ID_3rdParty                  | 0.82                |
| Identifier_Cookie_or_similar_Tech_1stParty | 0.81                |
| Identifier_Cookie_or_similar_Tech_3rdParty | 0.76                |
| Identifier_Device_ID_1stParty              | 0.69                |
| Identifier_Device_ID_3rdParty              | 0.76                |
| Identifier_IMEI_1stParty                   | 0.94                |
| Identifier_IMEI_3rdParty                   | 0.79                |
| Identifier_IMSI_1stParty                   | 0.9                 |
| Identifier_IMSI_3rdParty                   | 1                   |
| Identifier_IP_Address_1stParty             | 0.76                |
| Identifier_IP_Address_3rdParty             | 0.65                |
| Identifier_MAC_1stParty                    | 0.73                |
| Identifier_MAC_3rdParty                    | 0.89                |
| Identifier_Mobile_Carrier_1stParty         | 0.82                |
| Identifier_Mobile_Carrier_3rdParty         | 0.76                |
| Identifier_SIM_Serial_1stParty             | 0.65                |
| Identifier_SIM_Serial_3rdParty             | 0.49                |
| Identifier_SSID_BSSID_1stParty             | 1                   |
| Identifier_SSID_BSSID_3rdParty             | 1                   |
| Location_1stParty                          | 0.67                |
| Location_3rdParty                          | 0.71                |
| Location_Bluetooth_1stParty                | 0.78                |
| Location_Bluetooth_3rdParty                | 0.89                |
| Location_Cell_Tower_1stParty               | 0.66                |
| Location_Cell_Tower_3rdParty               | 0.89                |
| Location_GPS_1stParty                      | 0.85                |
| Location_GPS_3rdParty                      | 0.92                |
| Location_IP_Address_1stParty               | 0.4                 |
| Location_IP_Address_3rdParty               | 0.66                |
| Location_WiFi_1stParty                     | 0.77                |
| Location_WiFi_3rdParty                     | 0.8                 |
| SSO                                        | 0.64                |
| Facebook_SSO                               | 0.78                |


For some of the practices with agreement below 0.67 we calculated whether the annotators systematically disagreed with each other. Low levels of agreement do not necessarily present a problem; classifiers can achieve good performance despite being trained on data with low inter-annotator agreement, so long as the disagreement looks like random noise [1]. In order to evaluate whether systematic agreement exists we are using the following methodology [2]:

> To analyze whether disagreements contain systematic patterns we evaluate how often each annotator disagrees with the other two annotators. If he or she is in a minority position for a statistically significant number of times, there might be a misunderstanding of the annotation task or other systematic reason for disagreement. However, if there is no systematic disagreement, annotations are reliable despite low agreement levels. Assuming a uniform distribution each annotator should be in the minority in 1/3 of all disagreements. We test this assumption with the binomial test for goodness of fit. Specifically, we use the binomial distribution to calculate the probability of an annotator being x or more times in the minority by adding up the probability of being exactly x times in the minority, being x + 1 times in the minority, up to x + n (that is, being always in the minority), and comparing the result to the expected probability of 1/3. We use a one-tailed test as we are not interested in finding whether an annotator is fewer times in the minority than in 1/3 of the disagreements. An annotator can be in the minority when omitting an annotation that the two other annotators made or adding an extra annotation.

| Privacy Practice               | Additional Annotation p value | Omitted Annotation p value |
| ------------------------------ | ----------------------------- |--------------------------- |
| Contact_3rdParty               | 0.56                          | 0.56                       |
| Identifier_1stParty            | 0.17                          | 0.56                       |
| Identifier_3rdParty            | 0.54                          | 0.56                       |
| Identifier_IP_Address_3rdParty | 0.11                          | 0.05                       |
| Identifier_SIM_Serial_1stParty | 0.11                          | 0.26                       |
| Identifier_SIM_Serial_3rdParty | N/A <sup>*</sup>              | 0.33                       |
| Location_Cell_Tower_1stParty   | 0.56                          | 0.41                       |
| SSO                            | 0.17                          | 0.56                       |

<sup>*</sup> The disagreement cannot be calculated because there is no instance of one annotator annotating a segment while the other two annotators omitted it.

[1] Dennis Reidsma and Jean Carletta. "Reliability measurement without limits." Computational Linguistics 34, no. 3 (2008): 319-326.

[2] Sebastian Zimmeck, Ziqi Wang, Lieyong Zou, Roger Iyengar, Bin Liu, Florian Schaub, Shomir Wilson, Norman Sadeh, Steven M. Bellovin, and Joel Reidenberg. "Automated Analysis of Privacy Requirements for Mobile Apps." 24th Network & Distributed System Security Symposium (NDSS).
