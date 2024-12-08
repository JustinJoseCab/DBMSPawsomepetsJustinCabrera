# DBMSPawsomepetsJustinCabrera

This database is for Project 1 of DSC623.
We were tasked with creating a ER model, Logical Model and Implementation of the the Pawsome Pets Case study. 

Attached is the ER report, the Logical Model report and the py file of the final implementation. \

Case Study:
A company called Pawsome Pets runs multiple clinics. The company would like for their data
to be stored in a database. The following description was obtained during the analysis phase:
“Each of the Pawsome Pets clinics has several staff members and a member of staff manages
at most one clinic (not all staff manage clinics). Each clinic has a unique clinic number
(clinicNo) and each member of staff has a unique staff number (staffNo). Additionally, the
company would like to store each clinic’s name, address and telephone number, as well as the
staff’s name, address, telephone number, DOB, position and salary.
When a pet owner contacts a clinic, the owner’s pet is registered with the clinic. An owner can
own one or more pets, but a pet can only be registered at one clinic. Each owner has a unique
owner number (ownerNo), a name, an address and a telephone number. Each pet has a unique
pet number (petNo), name, DOB, animal species, breed and color.
When the pet comes to the clinic, it undergoes an examination by a member of the consulting
staff. The database should store the following information for each examination: chief
complaint (i.e., the main cause for the visit), description (i.e., what was done during the
examination), date seen and actions taken (e.g., a treatment was prescribed, tests were
ordered). A unique examination number (examNo) is assigned to each examination.
