#mean cell indices are used to classify types of anemia,
#they include mean cell volume,
#mean cell hemoglobin, mean cell hemoglobin concentration

packed_cell_volume = input("What is the hematocrit of the patient? ")
#the packed cell volume should be in litre per litre
packed_cell_volume= float(packed_cell_volume)
question = input("is the packed cell volume in litre per litre? (Y/N) ")
if (question.lower() == 'n'):
    packed_cell_volume = (packed_cell_volume/100)

hemoglobin = input ("What is the hemoglobin of the patient? ")
#the hemoglobin should be in g/dl
question_2 = input("is the hemoglobin in g/dL?(Y/N) ")
if (question.lower() == 'n'):
    hemoglobin = (hemoglobin/10)
hemoglobin = float(hemoglobin)

red_blood_cell_number = input("What is the number of red blood cells present in patient's sample? ")
#the red_blood_cell_number should be in *10^9/l
red_blood_cell_number = float(red_blood_cell_number)

mean_cell_volume = (packed_cell_volume/red_blood_cell_number)
#conversion to fentolitre
print ("the mean cell volume is ", mean_cell_volume, "fentolitre")

mean_cell_hemoglobin = (hemoglobin/red_blood_cell_number)
print("the mean cell hemoglobin is ", mean_cell_hemoglobin, "picogram")

mean_cell_hemoglobin_concentration = (hemoglobin/packed_cell_volume)
print("the mean cell hemoglobin concentration is ", mean_cell_hemoglobin_concentration, "%")
