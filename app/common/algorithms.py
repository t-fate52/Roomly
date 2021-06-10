from app.models import RoomieTrait, UserTrait
from app.common.service import get_one_query
from app.common.traits import db_traits


# def trait_obj_to_list(traits):
#     # delattr(traits, '_sa_instance_state')
#     delattr(traits, 'id')
#     delattr(traits, 'user_id')
#     return traits


def match_traits(myId, hisId):

    # We need to match four things
    # What I want against what he has
    # RoomieTrait(myId) UserTrait(hisId)
    # What he wants against what I have
    # RoomieTriat(hisId) UserTriat(myId)
    # I need only their ids
    my_ideal_roomie = get_one_query(RoomieTrait, myId)
    candidate_user = get_one_query(UserTrait, hisId)
    my_traits = get_one_query(UserTrait, myId)
    candidate_user_ideal_roomie = get_one_query(RoomieTrait, hisId)

    my_matching_traits = []
    his_matching_trait = []

    for i in range(0, 13):
        perfect_roomie = getattr(my_ideal_roomie, db_traits[i])
        candidate_traits = str(getattr(candidate_user, db_traits[i]))
        my_own_traits = str(getattr(my_traits, db_traits[i]))
        candidate_perfect_roomie = getattr(
            candidate_user_ideal_roomie, db_traits[i])

        if perfect_roomie == 'Maybe' or perfect_roomie == 'Neutral' or perfect_roomie == candidate_traits:
            my_matching_traits.append(db_traits[i])

        if candidate_perfect_roomie == 'Maybe' or candidate_perfect_roomie == 'Neutral' or my_own_traits == candidate_perfect_roomie:
            his_matching_trait.append(db_traits[i])

    match = (len(my_matching_traits) + len(his_matching_trait)) * (100/26)

    return round(match)
