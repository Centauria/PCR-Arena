# coding: utf-8
from sqlalchemy import Column, Float, Index, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ActualUnitBackground(Base):
    __tablename__ = 'actual_unit_background'

    unit_id = Column(Integer, primary_key=True)
    unit_name = Column(Text, nullable=False)
    bg_id = Column(Integer, nullable=False)
    face_type = Column(Integer, nullable=False)


class AilmentDatum(Base):
    __tablename__ = 'ailment_data'

    ailment_id = Column(Integer, primary_key=True)
    ailment_action = Column(Integer, nullable=False)
    ailment_detail_1 = Column(Integer, nullable=False)
    ailment_name = Column(Text, nullable=False)


class AlbumProductionList(Base):
    __tablename__ = 'album_production_list'

    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, nullable=False, index=True)
    type = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)


class AlbumVoiceList(Base):
    __tablename__ = 'album_voice_list'

    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, nullable=False, index=True)
    sheet_id = Column(Text, nullable=False)
    voice_id = Column(Text, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)


class ArenaDailyRankReward(Base):
    __tablename__ = 'arena_daily_rank_reward'

    id = Column(Integer, primary_key=True)
    rank_from = Column(Integer, nullable=False)
    rank_to = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class ArenaDefenceReward(Base):
    __tablename__ = 'arena_defence_reward'

    id = Column(Integer, primary_key=True)
    limit_count = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class ArenaMaxRankReward(Base):
    __tablename__ = 'arena_max_rank_reward'

    id = Column(Integer, primary_key=True)
    rank_from = Column(Integer, nullable=False)
    rank_to = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class ArenaMaxSeasonRankReward(Base):
    __tablename__ = 'arena_max_season_rank_reward'

    id = Column(Integer, primary_key=True)
    rank_from = Column(Integer, nullable=False)
    rank_to = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class Banner(Base):
    __tablename__ = 'banner'

    banner_id = Column(Integer, primary_key=True)
    type = Column(Integer, nullable=False)
    system_id = Column(Integer, nullable=False)
    priority = Column(Integer, nullable=False)
    start_date = Column(Text, nullable=False)
    end_date = Column(Text, nullable=False)
    sub_banner_id_1 = Column(Integer, nullable=False)
    is_show_room = Column(Integer, nullable=False)


class BgDatum(Base):
    __tablename__ = 'bg_data'

    view_name = Column(Text, primary_key=True)
    bg_id = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)


class CampaignFreegacha(Base):
    __tablename__ = 'campaign_freegacha'

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, nullable=False)
    freegacha_1 = Column(Integer, nullable=False)
    freegacha_10 = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    stock_10_flag = Column(Integer, nullable=False)
    relation_id = Column(Integer, nullable=False)
    relation_count = Column(Integer, nullable=False)


class CampaignFreegachaDatum(Base):
    __tablename__ = 'campaign_freegacha_data'

    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, nullable=False)
    gacha_id = Column(Integer, nullable=False)


class CampaignSchedule(Base):
    __tablename__ = 'campaign_schedule'

    id = Column(Integer, primary_key=True)
    campaign_category = Column(Integer, nullable=False)
    value = Column(Float, nullable=False)
    system_id = Column(Integer, nullable=False)
    icon_image = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class CharaFortuneReward(Base):
    __tablename__ = 'chara_fortune_reward'

    id = Column(Integer, primary_key=True)
    fortune_id = Column(Integer, nullable=False)
    rank = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    count_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    count_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    count_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    count_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    count_5 = Column(Integer, nullable=False)


class CharaFortuneSchedule(Base):
    __tablename__ = 'chara_fortune_schedule'

    fortune_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class CharaIdentity(Base):
    __tablename__ = 'chara_identity'

    unit_id = Column(Integer, primary_key=True)
    chara_type = Column(Integer, nullable=False)


class CharaStoryStatu(Base):
    __tablename__ = 'chara_story_status'

    story_id = Column(Integer, primary_key=True)
    unlock_story_name = Column(Text, nullable=False)
    status_type_1 = Column(Integer, nullable=False)
    status_rate_1 = Column(Integer, nullable=False)
    status_type_2 = Column(Integer, nullable=False)
    status_rate_2 = Column(Integer, nullable=False)
    status_type_3 = Column(Integer, nullable=False)
    status_rate_3 = Column(Integer, nullable=False)
    status_type_4 = Column(Integer, nullable=False)
    status_rate_4 = Column(Integer, nullable=False)
    status_type_5 = Column(Integer, nullable=False)
    status_rate_5 = Column(Integer, nullable=False)
    chara_id_1 = Column(Integer, nullable=False)
    chara_id_2 = Column(Integer, nullable=False)
    chara_id_3 = Column(Integer, nullable=False)
    chara_id_4 = Column(Integer, nullable=False)
    chara_id_5 = Column(Integer, nullable=False)
    chara_id_6 = Column(Integer, nullable=False)
    chara_id_7 = Column(Integer, nullable=False)
    chara_id_8 = Column(Integer, nullable=False)
    chara_id_9 = Column(Integer, nullable=False)
    chara_id_10 = Column(Integer, nullable=False)


class CharacterLoveRankupText(Base):
    __tablename__ = 'character_love_rankup_text'

    chara_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    love_level = Column(Integer, nullable=False)
    scale = Column(Float, nullable=False)
    position_x = Column(Integer, nullable=False)
    position_y = Column(Integer, nullable=False)
    voice_id_1 = Column(Integer, nullable=False)
    face_1 = Column(Integer, nullable=False)
    serif_1 = Column(Text, nullable=False)
    voice_id_2 = Column(Integer, nullable=False)
    face_2 = Column(Integer, nullable=False)
    serif_2 = Column(Text, nullable=False)
    voice_id_3 = Column(Integer, nullable=False)
    face_3 = Column(Integer, nullable=False)
    serif_3 = Column(Text, nullable=False)


class ClanBattleBossDamageRank(Base):
    __tablename__ = 'clan_battle_boss_damage_rank'

    id = Column(Integer, nullable=False)
    damage_rank_id = Column(Integer, primary_key=True, nullable=False, index=True)
    ranking_from = Column(Integer, primary_key=True, nullable=False)
    ranking_to = Column(Integer, primary_key=True, nullable=False)
    odds_group_id = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class ClanBattleBossDatum(Base):
    __tablename__ = 'clan_battle_boss_data'

    boss_id = Column(Integer, primary_key=True)
    clan_battle_id = Column(Integer, nullable=False)
    difficulty = Column(Integer, nullable=False)
    order_num = Column(Integer, nullable=False)
    boss_thumb_id = Column(Integer, nullable=False)


class ClanBattleBossFixReward(Base):
    __tablename__ = 'clan_battle_boss_fix_reward'

    fix_reward_id = Column(Integer, primary_key=True)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class ClanBattleBossGroup(Base):
    __tablename__ = 'clan_battle_boss_group'

    clan_battle_boss_group_id = Column(Integer, primary_key=True, nullable=False, index=True)
    order_num = Column(Integer, primary_key=True, nullable=False)
    position_x = Column(Integer, nullable=False)
    position_y = Column(Integer, nullable=False)
    limit_time = Column(Integer, nullable=False)
    scale_ratio = Column(Float, nullable=False)
    map_position_x = Column(Integer, nullable=False)
    map_position_y = Column(Integer, nullable=False)
    cursor_position = Column(Integer, nullable=False)
    result_boss_position_y = Column(Integer, nullable=False)
    chest_id = Column(Integer, nullable=False)
    fix_reward_id = Column(Integer, nullable=False)
    damage_rank_id = Column(Integer, nullable=False)
    quest_detail_bg_id = Column(Integer, nullable=False)
    quest_detail_bg_position = Column(Integer, nullable=False)
    quest_detail_monster_size = Column(Float, nullable=False)
    quest_detail_monster_height = Column(Integer, nullable=False)
    battle_report_monster_size = Column(Float, nullable=False)
    battle_report_monster_height = Column(Integer, nullable=False)
    background = Column(Integer, nullable=False)
    wave_group_id = Column(Integer, nullable=False)
    reward_gold_coefficient = Column(Float, nullable=False)
    limited_mana = Column(Integer, nullable=False)
    wave_bgm = Column(Text, nullable=False)
    quest_detail_rehearsal_label_height = Column(Integer, nullable=False)
    last_attack_reward_id = Column(Integer, nullable=False)
    score_coefficient = Column(Float, nullable=False)
    min_carry_over_time = Column(Integer, nullable=False)


class ClanBattleHpResetCost(Base):
    __tablename__ = 'clan_battle_hp_reset_cost'

    id = Column(Integer, primary_key=True)
    reset_count_from = Column(Integer, nullable=False)
    reset_count_to = Column(Integer, nullable=False)
    cost_num = Column(Integer, nullable=False)


class ClanBattleLastAttackReward(Base):
    __tablename__ = 'clan_battle_last_attack_reward'

    last_attack_reward_id = Column(Integer, primary_key=True)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class ClanBattleMapDatum(Base):
    __tablename__ = 'clan_battle_map_data'

    id = Column(Integer, primary_key=True)
    clan_battle_id = Column(Integer, nullable=False)
    map_bg = Column(Integer, nullable=False)
    difficulty = Column(Integer, nullable=False)
    lap_num_from = Column(Integer, nullable=False)
    lap_num_to = Column(Integer, nullable=False)
    clan_battle_boss_group_id = Column(Integer, nullable=False)
    aura_effect = Column(Integer, nullable=False)
    rsl_unlock_lap = Column(Integer, nullable=False)
    phase = Column(Integer, nullable=False)


class ClanBattleOddsDatum(Base):
    __tablename__ = 'clan_battle_odds_data'

    odds_group_id = Column(Integer, primary_key=True, nullable=False, index=True)
    team_level_from = Column(Integer, primary_key=True, nullable=False)
    team_level_to = Column(Integer, primary_key=True, nullable=False)
    odds_csv_1 = Column(Text, nullable=False)
    odds_csv_2 = Column(Text, nullable=False)
    odds_csv_3 = Column(Text, nullable=False)
    odds_csv_4 = Column(Text, nullable=False)
    odds_csv_5 = Column(Text, nullable=False)
    odds_csv_6 = Column(Text, nullable=False)
    odds_csv_7 = Column(Text, nullable=False)
    odds_csv_8 = Column(Text, nullable=False)
    odds_csv_9 = Column(Text, nullable=False)
    odds_csv_10 = Column(Text, nullable=False)


class ClanBattlePeriod(Base):
    __tablename__ = 'clan_battle_period'

    clan_battle_id = Column(Integer, primary_key=True, nullable=False, index=True)
    period = Column(Integer, primary_key=True, nullable=False)
    period_detail = Column(Text, nullable=False)
    period_detail_bg = Column(Integer, nullable=False)
    period_detail_bg_position = Column(Integer, nullable=False)
    period_detail_boss_position_x = Column(Integer, nullable=False)
    period_detail_boss_position_y = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    interval_start = Column(Text, nullable=False)
    interval_end = Column(Text, nullable=False)
    calc_start = Column(Text, nullable=False)
    result_start = Column(Text, nullable=False)
    result_end = Column(Text, nullable=False)


class ClanBattlePeriodRankBonu(Base):
    __tablename__ = 'clan_battle_period_rank_bonus'

    ranking_bonus_group_id = Column(Integer, primary_key=True, nullable=False, index=True)
    rank_from = Column(Integer, primary_key=True, nullable=False)
    rank_to = Column(Integer, primary_key=True, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class ClanBattlePeriodRankReward(Base):
    __tablename__ = 'clan_battle_period_rank_reward'

    id = Column(Integer, primary_key=True)
    clan_battle_id = Column(Integer, nullable=False)
    period = Column(Integer, nullable=False)
    rank_from = Column(Integer, nullable=False)
    rank_to = Column(Integer, nullable=False)
    ranking_bonus_group = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class ClanBattleSchedule(Base):
    __tablename__ = 'clan_battle_schedule'

    clan_battle_id = Column(Integer, primary_key=True)
    release_month = Column(Integer, nullable=False)
    last_clan_battle_id = Column(Integer, nullable=False)
    point_per_stamina = Column(Integer, nullable=False)
    cost_group_id = Column(Integer, nullable=False)
    map_bgm = Column(Text, nullable=False)
    resource_id = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class ClanBattleTotalRank(Base):
    __tablename__ = 'clan_battle_total_rank'

    id = Column(Integer, primary_key=True)
    clan_battle_id = Column(Integer, nullable=False)
    rank_from = Column(Integer, nullable=False)
    rank_to = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class ClanCostGroup(Base):
    __tablename__ = 'clan_cost_group'

    id = Column(Integer, primary_key=True)
    cost_group_id = Column(Integer, nullable=False)
    difficulty = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)


class ClanGrade(Base):
    __tablename__ = 'clan_grade'

    clan_grade_id = Column(Integer, primary_key=True)
    rank_from = Column(Integer, nullable=False)
    rank_to = Column(Integer, nullable=False)


class ClanInviteLevelGroup(Base):
    __tablename__ = 'clan_invite_level_group'

    level_group_id = Column(Integer, primary_key=True)
    team_level_from = Column(Integer, nullable=False)
    team_level_to = Column(Integer, nullable=False)


class ContentMapDatum(Base):
    __tablename__ = 'content_map_data'

    content_map_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    map_type = Column(Integer, nullable=False)
    area_id = Column(Integer, nullable=False)
    condition_quest_id = Column(Integer, nullable=False)
    quest_position_x = Column(Integer, nullable=False)
    quest_position_y = Column(Integer, nullable=False)
    icon_id = Column(Integer, nullable=False)
    system_id = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class ContentReleaseDatum(Base):
    __tablename__ = 'content_release_data'

    system_id = Column(Integer, primary_key=True)
    team_level = Column(Integer, nullable=False)
    story_id = Column(Integer, nullable=False)
    quest_id = Column(Integer, nullable=False)
    dialog = Column(Text, nullable=False)


class CooperationQuestDatum(Base):
    __tablename__ = 'cooperation_quest_data'

    quest_id = Column(Integer, primary_key=True)
    quest_name = Column(Text, nullable=False)
    difficulty_level = Column(Integer, nullable=False)
    limit_team_level = Column(Integer, nullable=False)
    team_exp = Column(Integer, nullable=False)
    exp = Column(Integer, nullable=False)
    limit_time = Column(Integer, nullable=False)
    clear_reward_group_id = Column(Integer, nullable=False)
    odds_group_id = Column(Integer, nullable=False)
    lobby_background = Column(Integer, nullable=False)
    background_1 = Column(Integer, nullable=False)
    wave_group_id_1 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_1 = Column(Text, nullable=False)
    wave_bgm_que_id_1 = Column(Text, nullable=False)
    background_2 = Column(Integer, nullable=False)
    wave_group_id_2 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_2 = Column(Text, nullable=False)
    wave_bgm_que_id_2 = Column(Text, nullable=False)
    background_3 = Column(Integer, nullable=False)
    wave_group_id_3 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_3 = Column(Text, nullable=False)
    wave_bgm_que_id_3 = Column(Text, nullable=False)
    enemy_image_1 = Column(Integer, nullable=False)
    enemy_image_2 = Column(Integer, nullable=False)
    enemy_image_3 = Column(Integer, nullable=False)
    enemy_image_4 = Column(Integer, nullable=False)
    enemy_image_5 = Column(Integer, nullable=False)
    first_reward_image_1 = Column(Integer, nullable=False)
    first_reward_image_2 = Column(Integer, nullable=False)
    first_reward_image_3 = Column(Integer, nullable=False)
    first_reward_image_4 = Column(Integer, nullable=False)
    first_reward_image_5 = Column(Integer, nullable=False)
    repeat_reward_image_1 = Column(Integer, nullable=False)
    repeat_reward_image_2 = Column(Integer, nullable=False)
    repeat_reward_image_3 = Column(Integer, nullable=False)
    cooperation_quest_detail_bg_id = Column(Integer, nullable=False)
    cooperation_quest_detail_bg_position = Column(Integer, nullable=False)
    main_enemy_image_wave_1 = Column(Integer, nullable=False)
    sub_enemy_image_wave_1_1 = Column(Integer, nullable=False)
    sub_enemy_image_wave_1_2 = Column(Integer, nullable=False)
    sub_enemy_image_wave_1_3 = Column(Integer, nullable=False)
    sub_enemy_image_wave_1_4 = Column(Integer, nullable=False)
    main_enemy_image_wave_2 = Column(Integer, nullable=False)
    sub_enemy_image_wave_2_1 = Column(Integer, nullable=False)
    sub_enemy_image_wave_2_2 = Column(Integer, nullable=False)
    sub_enemy_image_wave_2_3 = Column(Integer, nullable=False)
    sub_enemy_image_wave_2_4 = Column(Integer, nullable=False)
    main_enemy_image_wave_3 = Column(Integer, nullable=False)
    sub_enemy_image_wave_3_1 = Column(Integer, nullable=False)
    sub_enemy_image_wave_3_2 = Column(Integer, nullable=False)
    sub_enemy_image_wave_3_3 = Column(Integer, nullable=False)
    sub_enemy_image_wave_3_4 = Column(Integer, nullable=False)
    quest_comment = Column(Text, nullable=False)
    unlock_quest_id_1 = Column(Integer, nullable=False)
    unlock_quest_id_2 = Column(Integer, nullable=False)


class DailyMissionDatum(Base):
    __tablename__ = 'daily_mission_data'

    daily_mission_id = Column(Integer, primary_key=True)
    disp_group = Column(Integer, nullable=False)
    category_icon = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    mission_condition = Column(Integer, nullable=False)
    condition_value_1 = Column(Integer)
    condition_value_2 = Column(Integer)
    condition_value_3 = Column(Integer)
    condition_num = Column(Integer, nullable=False)
    mission_reward_id = Column(Integer, nullable=False)
    system_id = Column(Integer)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class DungeonAreaDatum(Base):
    __tablename__ = 'dungeon_area_data'

    dungeon_area_id = Column(Integer, primary_key=True)
    dungeon_type = Column(Integer, nullable=False)
    dungeon_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    open_quest_id = Column(Integer, nullable=False)
    content_release_story = Column(Integer, nullable=False)
    initial_clear_story = Column(Integer, nullable=False)
    wave_group_id = Column(Integer, nullable=False)
    reward_group_id = Column(Integer, nullable=False)
    recommend_level = Column(Integer, nullable=False)
    quest_position_x = Column(Integer, nullable=False)
    quest_position_y = Column(Integer, nullable=False)
    icon_id = Column(Integer, nullable=False)
    coin_item_id = Column(Integer, nullable=False)
    enemy_image_1 = Column(Integer, nullable=False)
    enemy_image_2 = Column(Integer, nullable=False)
    enemy_image_3 = Column(Integer, nullable=False)
    enemy_image_4 = Column(Integer, nullable=False)
    enemy_image_5 = Column(Integer, nullable=False)
    view_reward_id_1 = Column(Integer, nullable=False)
    view_reward_id_2 = Column(Integer, nullable=False)
    view_reward_id_3 = Column(Integer, nullable=False)
    view_reward_id_4 = Column(Integer, nullable=False)
    view_reward_id_5 = Column(Integer, nullable=False)
    recovery_hp_rate = Column(Integer, nullable=False)
    recovery_tp_rate = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class DungeonQuestDatum(Base):
    __tablename__ = 'dungeon_quest_data'

    quest_id = Column(Integer, primary_key=True)
    dungeon_area_id = Column(Integer, nullable=False)
    floor_num = Column(Integer, nullable=False)
    limit_time = Column(Integer, nullable=False)
    matching_coefficient = Column(Float, nullable=False)
    reward_image_1 = Column(Integer, nullable=False)
    reward_image_2 = Column(Integer, nullable=False)
    reward_image_3 = Column(Integer, nullable=False)
    reward_coin = Column(Integer, nullable=False)
    chest_id = Column(Integer, nullable=False)
    odds_group_id = Column(Integer, nullable=False)
    background = Column(Integer, nullable=False)
    dungeon_quest_detail_bg_id = Column(Integer, nullable=False)
    dungeon_quest_detail_bg_position = Column(Integer, nullable=False)
    dungeon_quest_detail_monster_size = Column(Float, nullable=False)
    dungeon_quest_detail_monster_height = Column(Float, nullable=False)
    wave_bgm_sheet_id_1 = Column(Text, nullable=False)
    wave_bgm_que_id_1 = Column(Text, nullable=False)


class EmblemDatum(Base):
    __tablename__ = 'emblem_data'

    emblem_id = Column(Integer, primary_key=True)
    disp_oder = Column(Integer, nullable=False)
    type = Column(Integer, nullable=False)
    emblem_name = Column(Text, nullable=False)
    description_mission_id = Column(Integer, nullable=False)
    event_emblem = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class EmblemMissionDatum(Base):
    __tablename__ = 'emblem_mission_data'

    mission_id = Column(Integer, primary_key=True)
    disp_group = Column(Integer, nullable=False)
    category_icon = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    mission_condition = Column(Integer, nullable=False)
    condition_value_1 = Column(Integer, nullable=False)
    condition_value_2 = Column(Integer, nullable=False)
    condition_value_3 = Column(Integer, nullable=False)
    condition_num = Column(Integer, nullable=False)
    mission_reward_id = Column(Integer, nullable=False)
    system_id = Column(Integer, nullable=False)
    visible_flag = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class EmblemMissionRewardDatum(Base):
    __tablename__ = 'emblem_mission_reward_data'

    id = Column(Integer, primary_key=True)
    mission_reward_id = Column(Integer, nullable=False, index=True)
    reward_type = Column(Integer, nullable=False)
    reward_id = Column(Integer, nullable=False, index=True)
    reward_num = Column(Integer, nullable=False)
    icon_type = Column(Integer, nullable=False)


class EnemyParameter(Base):
    __tablename__ = 'enemy_parameter'

    enemy_id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, nullable=False)
    name = Column(Text, nullable=False)
    level = Column(Integer, nullable=False)
    rarity = Column(Integer, nullable=False)
    promotion_level = Column(Integer, nullable=False)
    hp = Column(Integer, nullable=False)
    atk = Column(Integer, nullable=False)
    magic_str = Column(Integer, nullable=False)
    _def = Column('def', Integer, nullable=False)
    magic_def = Column(Integer, nullable=False)
    physical_critical = Column(Integer, nullable=False)
    magic_critical = Column(Integer, nullable=False)
    wave_hp_recovery = Column(Integer, nullable=False)
    wave_energy_recovery = Column(Integer, nullable=False)
    dodge = Column(Integer, nullable=False)
    physical_penetrate = Column(Integer, nullable=False)
    magic_penetrate = Column(Integer, nullable=False)
    life_steal = Column(Integer, nullable=False)
    hp_recovery_rate = Column(Integer, nullable=False)
    energy_recovery_rate = Column(Integer, nullable=False)
    energy_reduce_rate = Column(Integer, nullable=False)
    union_burst_level = Column(Integer, nullable=False)
    main_skill_lv_1 = Column(Integer, nullable=False)
    main_skill_lv_2 = Column(Integer, nullable=False)
    main_skill_lv_3 = Column(Integer, nullable=False)
    main_skill_lv_4 = Column(Integer, nullable=False)
    main_skill_lv_5 = Column(Integer, nullable=False)
    main_skill_lv_6 = Column(Integer, nullable=False)
    main_skill_lv_7 = Column(Integer, nullable=False)
    main_skill_lv_8 = Column(Integer, nullable=False)
    main_skill_lv_9 = Column(Integer, nullable=False)
    main_skill_lv_10 = Column(Integer, nullable=False)
    ex_skill_lv_1 = Column(Integer, nullable=False)
    ex_skill_lv_2 = Column(Integer, nullable=False)
    ex_skill_lv_3 = Column(Integer, nullable=False)
    ex_skill_lv_4 = Column(Integer, nullable=False)
    ex_skill_lv_5 = Column(Integer, nullable=False)
    resist_status_id = Column(Integer, nullable=False)
    accuracy = Column(Integer, nullable=False)


class EnemyRewardDatum(Base):
    __tablename__ = 'enemy_reward_data'

    drop_reward_id = Column(Integer, primary_key=True)
    drop_count = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    odds_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    odds_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    odds_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    odds_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)
    odds_5 = Column(Integer, nullable=False)


class EquipmentCraft(Base):
    __tablename__ = 'equipment_craft'

    equipment_id = Column(Integer, primary_key=True)
    crafted_cost = Column(Integer, nullable=False)
    condition_equipment_id_1 = Column(Integer, nullable=False)
    consume_num_1 = Column(Integer, nullable=False)
    condition_equipment_id_2 = Column(Integer, nullable=False)
    consume_num_2 = Column(Integer, nullable=False)
    condition_equipment_id_3 = Column(Integer, nullable=False)
    consume_num_3 = Column(Integer, nullable=False)
    condition_equipment_id_4 = Column(Integer, nullable=False)
    consume_num_4 = Column(Integer, nullable=False)
    condition_equipment_id_5 = Column(Integer, nullable=False)
    consume_num_5 = Column(Integer, nullable=False)
    condition_equipment_id_6 = Column(Integer, nullable=False)
    consume_num_6 = Column(Integer, nullable=False)
    condition_equipment_id_7 = Column(Integer, nullable=False)
    consume_num_7 = Column(Integer, nullable=False)
    condition_equipment_id_8 = Column(Integer, nullable=False)
    consume_num_8 = Column(Integer, nullable=False)
    condition_equipment_id_9 = Column(Integer, nullable=False)
    consume_num_9 = Column(Integer, nullable=False)
    condition_equipment_id_10 = Column(Integer, nullable=False)
    consume_num_10 = Column(Integer, nullable=False)


class EquipmentDatum(Base):
    __tablename__ = 'equipment_data'

    equipment_id = Column(Integer, primary_key=True)
    equipment_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    promotion_level = Column(Integer, nullable=False)
    craft_flg = Column(Integer, nullable=False)
    equipment_enhance_point = Column(Integer, nullable=False)
    sale_price = Column(Integer, nullable=False)
    require_level = Column(Integer, nullable=False)
    hp = Column(Float, nullable=False)
    atk = Column(Float, nullable=False)
    magic_str = Column(Float, nullable=False)
    _def = Column('def', Float, nullable=False)
    magic_def = Column(Float, nullable=False)
    physical_critical = Column(Float, nullable=False)
    magic_critical = Column(Float, nullable=False)
    wave_hp_recovery = Column(Float, nullable=False)
    wave_energy_recovery = Column(Float, nullable=False)
    dodge = Column(Float, nullable=False)
    physical_penetrate = Column(Float, nullable=False)
    magic_penetrate = Column(Float, nullable=False)
    life_steal = Column(Float, nullable=False)
    hp_recovery_rate = Column(Float, nullable=False)
    energy_recovery_rate = Column(Float, nullable=False)
    energy_reduce_rate = Column(Float, nullable=False)
    enable_donation = Column(Integer, nullable=False)
    accuracy = Column(Float, nullable=False)


class EquipmentDonation(Base):
    __tablename__ = 'equipment_donation'

    team_level = Column(Integer, primary_key=True)
    donation_num_once = Column(Integer, nullable=False)
    donation_num_daily = Column(Integer, nullable=False)
    request_num_once = Column(Integer, nullable=False)


class EquipmentEnhanceDatum(Base):
    __tablename__ = 'equipment_enhance_data'

    promotion_level = Column(Integer, primary_key=True, nullable=False)
    equipment_enhance_level = Column(Integer, primary_key=True, nullable=False)
    needed_point = Column(Integer, nullable=False)
    total_point = Column(Integer, nullable=False)


class EquipmentEnhanceRate(Base):
    __tablename__ = 'equipment_enhance_rate'

    equipment_id = Column(Integer, primary_key=True)
    equipment_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    promotion_level = Column(Integer, nullable=False)
    hp = Column(Float, nullable=False)
    atk = Column(Float, nullable=False)
    magic_str = Column(Float, nullable=False)
    _def = Column('def', Float, nullable=False)
    magic_def = Column(Float, nullable=False)
    physical_critical = Column(Float, nullable=False)
    magic_critical = Column(Float, nullable=False)
    wave_hp_recovery = Column(Float, nullable=False)
    wave_energy_recovery = Column(Float, nullable=False)
    dodge = Column(Float, nullable=False)
    physical_penetrate = Column(Float, nullable=False)
    magic_penetrate = Column(Float, nullable=False)
    life_steal = Column(Float, nullable=False)
    hp_recovery_rate = Column(Float, nullable=False)
    energy_recovery_rate = Column(Float, nullable=False)
    energy_reduce_rate = Column(Float, nullable=False)
    accuracy = Column(Float, nullable=False)


class EventBgDatum(Base):
    __tablename__ = 'event_bg_data'

    event_id = Column(Integer, primary_key=True)
    bg_id = Column(Integer, nullable=False)
    start_date = Column(Text, nullable=False)
    end_date = Column(Text, nullable=False)


class EventBossTreasureBox(Base):
    __tablename__ = 'event_boss_treasure_box'

    event_boss_treasure_box_id = Column(Integer, primary_key=True)
    treasure_type_1 = Column(Integer, nullable=False)
    event_boss_treasure_content_id_1 = Column(Integer, nullable=False)
    each_odds_1 = Column(Integer, nullable=False)
    treasure_type_2 = Column(Integer, nullable=False)
    event_boss_treasure_content_id_2 = Column(Integer, nullable=False)
    each_odds_2 = Column(Integer, nullable=False)
    treasure_type_3 = Column(Integer, nullable=False)
    event_boss_treasure_content_id_3 = Column(Integer, nullable=False)
    each_odds_3 = Column(Integer, nullable=False)
    treasure_type_4 = Column(Integer, nullable=False)
    event_boss_treasure_content_id_4 = Column(Integer, nullable=False)
    each_odds_4 = Column(Integer, nullable=False)
    treasure_type_5 = Column(Integer, nullable=False)
    event_boss_treasure_content_id_5 = Column(Integer, nullable=False)
    each_odds_5 = Column(Integer, nullable=False)
    treasure_type_6 = Column(Integer, nullable=False)
    event_boss_treasure_content_id_6 = Column(Integer, nullable=False)
    each_odds_6 = Column(Integer, nullable=False)
    treasure_type_7 = Column(Integer, nullable=False)
    event_boss_treasure_content_id_7 = Column(Integer, nullable=False)
    each_odds_7 = Column(Integer, nullable=False)
    treasure_type_8 = Column(Integer, nullable=False)
    event_boss_treasure_content_id_8 = Column(Integer, nullable=False)
    each_odds_8 = Column(Integer, nullable=False)
    treasure_type_9 = Column(Integer, nullable=False)
    event_boss_treasure_content_id_9 = Column(Integer, nullable=False)
    each_odds_9 = Column(Integer, nullable=False)
    treasure_type_10 = Column(Integer, nullable=False)
    event_boss_treasure_content_id_10 = Column(Integer, nullable=False)
    each_odds_10 = Column(Integer, nullable=False)


class EventBossTreasureContent(Base):
    __tablename__ = 'event_boss_treasure_content'

    event_boss_treasure_content_id = Column(Integer, primary_key=True)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    odds_file_1 = Column(Text, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    odds_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    odds_file_2 = Column(Text, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    odds_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    odds_file_3 = Column(Text, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    odds_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    odds_file_4 = Column(Text, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    odds_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    odds_file_5 = Column(Text, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)
    odds_5 = Column(Integer, nullable=False)


class EventEnemyParameter(Base):
    __tablename__ = 'event_enemy_parameter'

    enemy_id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, nullable=False)
    level = Column(Integer, nullable=False)
    rarity = Column(Integer, nullable=False)
    promotion_level = Column(Integer, nullable=False)
    hp = Column(Integer, nullable=False)
    atk = Column(Integer, nullable=False)
    magic_str = Column(Integer, nullable=False)
    _def = Column('def', Integer, nullable=False)
    magic_def = Column(Integer, nullable=False)
    physical_critical = Column(Integer, nullable=False)
    magic_critical = Column(Integer, nullable=False)
    wave_hp_recovery = Column(Integer, nullable=False)
    wave_energy_recovery = Column(Integer, nullable=False)
    dodge = Column(Integer, nullable=False)
    physical_penetrate = Column(Integer, nullable=False)
    magic_penetrate = Column(Integer, nullable=False)
    life_steal = Column(Integer, nullable=False)
    hp_recovery_rate = Column(Integer, nullable=False)
    energy_recovery_rate = Column(Integer, nullable=False)
    energy_reduce_rate = Column(Integer, nullable=False)
    union_burst_level = Column(Integer, nullable=False)
    main_skill_lv_1 = Column(Integer, nullable=False)
    main_skill_lv_2 = Column(Integer, nullable=False)
    main_skill_lv_3 = Column(Integer, nullable=False)
    main_skill_lv_4 = Column(Integer, nullable=False)
    main_skill_lv_5 = Column(Integer, nullable=False)
    main_skill_lv_6 = Column(Integer, nullable=False)
    main_skill_lv_7 = Column(Integer, nullable=False)
    main_skill_lv_8 = Column(Integer, nullable=False)
    main_skill_lv_9 = Column(Integer, nullable=False)
    main_skill_lv_10 = Column(Integer, nullable=False)
    ex_skill_lv_1 = Column(Integer, nullable=False)
    ex_skill_lv_2 = Column(Integer, nullable=False)
    ex_skill_lv_3 = Column(Integer, nullable=False)
    ex_skill_lv_4 = Column(Integer, nullable=False)
    ex_skill_lv_5 = Column(Integer, nullable=False)
    resist_status_id = Column(Integer, nullable=False)
    accuracy = Column(Integer, nullable=False)


class EventEnemyRewardGroup(Base):
    __tablename__ = 'event_enemy_reward_group'

    id = Column(Integer, primary_key=True)
    reward_group_id = Column(Integer, nullable=False)
    reward_type = Column(Integer, nullable=False)
    reward_id = Column(Integer, nullable=False)
    reward_num = Column(Integer, nullable=False)
    odds = Column(Integer, nullable=False)


class EventGachaDatum(Base):
    __tablename__ = 'event_gacha_data'

    gacha_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    gacha_name = Column(Text, nullable=False)
    item_type = Column(Integer, nullable=False)
    item_id = Column(Integer, nullable=False)
    cost = Column(Integer, nullable=False)
    repeat_step = Column(Integer, nullable=False)


class EventIntroduction(Base):
    __tablename__ = 'event_introduction'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    introduction_number = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    maximum_chunk_size_1 = Column(Integer, nullable=False)
    maximum_chunk_size_loop_1 = Column(Integer, nullable=False)
    maximum_chunk_size_2 = Column(Integer, nullable=False)
    maximum_chunk_size_loop_2 = Column(Integer, nullable=False)
    maximum_chunk_size_3 = Column(Integer, nullable=False)
    maximum_chunk_size_loop_3 = Column(Integer, nullable=False)
    sheet_id = Column(Text, nullable=False)
    que_id = Column(Text, nullable=False)


class EventNaviComment(Base):
    __tablename__ = 'event_navi_comment'

    comment_id = Column(Integer, primary_key=True)
    where_type = Column(Integer, nullable=False)
    character_id = Column(Integer, nullable=False)
    face_type = Column(Integer, nullable=False)
    character_name = Column(Text, nullable=False)
    description = Column(Text)
    voice_id = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    pos_x = Column(Float, nullable=False)
    pos_y = Column(Float, nullable=False)
    change_face_time = Column(Float, nullable=False)
    change_face_type = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)


class EventNaviCommentCondition(Base):
    __tablename__ = 'event_navi_comment_condition'

    comment_id = Column(Integer, primary_key=True)
    condition_type_1 = Column(Integer, nullable=False)
    condition_value_1 = Column(Integer, nullable=False)
    condition_type_2 = Column(Integer, nullable=False)
    condition_value_2 = Column(Integer, nullable=False)
    condition_type_3 = Column(Integer, nullable=False)
    condition_value_3 = Column(Integer, nullable=False)


class EventStoryDatum(Base):
    __tablename__ = 'event_story_data'

    story_group_id = Column(Integer, primary_key=True)
    story_type = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False, index=True)
    title = Column(Text, nullable=False)
    thumbnail_id = Column(Integer, nullable=False)
    disp_order = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class EventStoryDetail(Base):
    __tablename__ = 'event_story_detail'

    story_id = Column(Integer, primary_key=True)
    story_group_id = Column(Integer, nullable=False, index=True)
    title = Column(Text, nullable=False)
    sub_title = Column(Text, nullable=False)
    visible_type = Column(Integer, nullable=False)
    story_end = Column(Integer, nullable=False)
    pre_story_id = Column(Integer, nullable=False)
    love_level = Column(Integer, nullable=False)
    requirement_id = Column(Integer, nullable=False)
    unlock_quest_id = Column(Integer, nullable=False)
    story_quest_id = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_value_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_value_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_value_3 = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class EventTopAdv(Base):
    __tablename__ = 'event_top_adv'
    __table_args__ = (
        Index('event_top_adv_0_event_id_1_type', 'event_id', 'type'),
    )

    event_top_adv_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    type = Column(Integer, nullable=False)
    value_1 = Column(Integer, nullable=False)
    value_2 = Column(Integer, nullable=False)
    value_3 = Column(Integer, nullable=False)
    story_id = Column(Integer, nullable=False)
    character_id = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class EventWaveGroupDatum(Base):
    __tablename__ = 'event_wave_group_data'

    id = Column(Integer, primary_key=True)
    wave_group_id = Column(Integer, nullable=False)
    difficulty = Column(Integer, nullable=False)
    wave = Column(Integer, nullable=False)
    match_lv_min = Column(Integer, nullable=False)
    match_lv_max = Column(Integer, nullable=False)
    enemy_id_1 = Column(Integer, nullable=False)
    enemy_id_2 = Column(Integer, nullable=False)
    enemy_id_3 = Column(Integer, nullable=False)
    enemy_id_4 = Column(Integer, nullable=False)
    enemy_id_5 = Column(Integer, nullable=False)
    drop_gold_1 = Column(Integer, nullable=False)
    reward_group_id_1 = Column(Integer, nullable=False)
    disp_reward_type_1 = Column(Integer, nullable=False)
    disp_reward_id_1 = Column(Integer, nullable=False)
    reward_lot_count_1 = Column(Integer, nullable=False)
    reward_odds_1 = Column(Integer, nullable=False)
    drop_gold_2 = Column(Integer, nullable=False)
    reward_group_id_2 = Column(Integer, nullable=False)
    disp_reward_type_2 = Column(Integer, nullable=False)
    disp_reward_id_2 = Column(Integer, nullable=False)
    reward_lot_count_2 = Column(Integer, nullable=False)
    reward_odds_2 = Column(Integer, nullable=False)
    drop_gold_3 = Column(Integer, nullable=False)
    reward_group_id_3 = Column(Integer, nullable=False)
    disp_reward_type_3 = Column(Integer, nullable=False)
    disp_reward_id_3 = Column(Integer, nullable=False)
    reward_lot_count_3 = Column(Integer, nullable=False)
    reward_odds_3 = Column(Integer, nullable=False)
    drop_gold_4 = Column(Integer, nullable=False)
    reward_group_id_4 = Column(Integer, nullable=False)
    disp_reward_type_4 = Column(Integer, nullable=False)
    disp_reward_id_4 = Column(Integer, nullable=False)
    reward_lot_count_4 = Column(Integer, nullable=False)
    reward_odds_4 = Column(Integer, nullable=False)
    drop_gold_5 = Column(Integer, nullable=False)
    reward_group_id_5 = Column(Integer, nullable=False)
    disp_reward_type_5 = Column(Integer, nullable=False)
    disp_reward_id_5 = Column(Integer, nullable=False)
    reward_lot_count_5 = Column(Integer, nullable=False)
    reward_odds_5 = Column(Integer, nullable=False)


class ExperienceTeam(Base):
    __tablename__ = 'experience_team'

    team_level = Column(Integer, primary_key=True)
    total_exp = Column(Integer, nullable=False)
    max_stamina = Column(Integer, nullable=False)
    over_limit_stamina = Column(Integer, nullable=False)
    recover_stamina_count = Column(Integer, nullable=False)


class ExperienceUnit(Base):
    __tablename__ = 'experience_unit'

    unit_level = Column(Integer, primary_key=True)
    total_exp = Column(Integer, nullable=False)


class FixLineupGroupSet(Base):
    __tablename__ = 'fix_lineup_group_set'
    __table_args__ = (
        Index('fix_lineup_group_set_0_team_level_from_1_team_level_to', 'team_level_from', 'team_level_to'),
    )

    lineup_group_set_id = Column(Integer, primary_key=True, nullable=False)
    team_level_from = Column(Integer, primary_key=True, nullable=False)
    team_level_to = Column(Integer, primary_key=True, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_count_1 = Column(Integer, nullable=False)
    price_type_1 = Column(Integer, nullable=False)
    currency_id_1 = Column(Integer, nullable=False)
    price_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_count_2 = Column(Integer, nullable=False)
    price_type_2 = Column(Integer, nullable=False)
    currency_id_2 = Column(Integer, nullable=False)
    price_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_count_3 = Column(Integer, nullable=False)
    price_type_3 = Column(Integer, nullable=False)
    currency_id_3 = Column(Integer, nullable=False)
    price_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_count_4 = Column(Integer, nullable=False)
    price_type_4 = Column(Integer, nullable=False)
    currency_id_4 = Column(Integer, nullable=False)
    price_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_count_5 = Column(Integer, nullable=False)
    price_type_5 = Column(Integer, nullable=False)
    currency_id_5 = Column(Integer, nullable=False)
    price_5 = Column(Integer, nullable=False)
    reward_type_6 = Column(Integer, nullable=False)
    reward_id_6 = Column(Integer, nullable=False)
    reward_count_6 = Column(Integer, nullable=False)
    price_type_6 = Column(Integer, nullable=False)
    currency_id_6 = Column(Integer, nullable=False)
    price_6 = Column(Integer, nullable=False)
    reward_type_7 = Column(Integer, nullable=False)
    reward_id_7 = Column(Integer, nullable=False)
    reward_count_7 = Column(Integer, nullable=False)
    price_type_7 = Column(Integer, nullable=False)
    currency_id_7 = Column(Integer, nullable=False)
    price_7 = Column(Integer, nullable=False)
    reward_type_8 = Column(Integer, nullable=False)
    reward_id_8 = Column(Integer, nullable=False)
    reward_count_8 = Column(Integer, nullable=False)
    price_type_8 = Column(Integer, nullable=False)
    currency_id_8 = Column(Integer, nullable=False)
    price_8 = Column(Integer, nullable=False)
    reward_type_9 = Column(Integer, nullable=False)
    reward_id_9 = Column(Integer, nullable=False)
    reward_count_9 = Column(Integer, nullable=False)
    price_type_9 = Column(Integer, nullable=False)
    currency_id_9 = Column(Integer, nullable=False)
    price_9 = Column(Integer, nullable=False)
    reward_type_10 = Column(Integer, nullable=False)
    reward_id_10 = Column(Integer, nullable=False)
    reward_count_10 = Column(Integer, nullable=False)
    price_type_10 = Column(Integer, nullable=False)
    currency_id_10 = Column(Integer, nullable=False)
    price_10 = Column(Integer, nullable=False)


class GachaDatum(Base):
    __tablename__ = 'gacha_data'

    gacha_id = Column(Integer, primary_key=True)
    gacha_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    gacha_detail = Column(Integer, nullable=False)
    gacha_cost_type = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    free_gacha_type = Column(Integer, nullable=False)
    free_gacha_interval_time = Column(Integer, nullable=False)
    free_gacha_count = Column(Integer, nullable=False)
    discount_price = Column(Integer, nullable=False)
    gacha_odds = Column(Text, nullable=False)
    gacha_odds_star2 = Column(Text, nullable=False)
    gacha_type = Column(Integer, nullable=False)
    movie_id = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    ticket_id = Column(Integer, nullable=False)
    special_id = Column(Integer, nullable=False)
    exchange_id = Column(Integer, nullable=False)
    ticket_id_10 = Column(Integer, nullable=False)
    rarity_odds = Column(Text, nullable=False)
    chara_odds_star1 = Column(Text, nullable=False)
    chara_odds_star2 = Column(Text, nullable=False)
    chara_odds_star3 = Column(Text, nullable=False)


class GachaExchangeLineup(Base):
    __tablename__ = 'gacha_exchange_lineup'

    id = Column(Integer, primary_key=True)
    exchange_id = Column(Integer, nullable=False)
    unit_id = Column(Integer, nullable=False)
    rarity = Column(Integer, nullable=False)


class GiftMessage(Base):
    __tablename__ = 'gift_message'

    id = Column(Integer, primary_key=True)
    discription = Column(Text, nullable=False)
    type_1 = Column(Integer, nullable=False)
    type_2 = Column(Integer, nullable=False)
    type_3 = Column(Integer, nullable=False)
    type_4 = Column(Integer, nullable=False)


class GlobalDatum(Base):
    __tablename__ = 'global_data'

    key_name = Column(Text, primary_key=True)
    value = Column(Integer, nullable=False)
    desc = Column(Text, nullable=False)


class GoldsetDatum(Base):
    __tablename__ = 'goldset_data'

    id = Column(Integer, nullable=False)
    buy_count = Column(Integer, primary_key=True)
    use_jewel_count = Column(Integer, nullable=False)
    get_gold_count = Column(Integer, nullable=False)
    goldset_odds_1 = Column(Integer, nullable=False)
    goldset_odds_2 = Column(Integer, nullable=False)
    goldset_odds_3 = Column(Integer, nullable=False)
    additional_gold_min_rate = Column(Integer, nullable=False)
    additional_gold_max_rate = Column(Integer, nullable=False)


class GoldsetDataTeamlevel(Base):
    __tablename__ = 'goldset_data_teamlevel'

    id = Column(Integer, nullable=False)
    team_level = Column(Integer, primary_key=True)
    initial_get_gold_count = Column(Integer, nullable=False)


class GrandArenaDailyRankReward(Base):
    __tablename__ = 'grand_arena_daily_rank_reward'

    id = Column(Integer, primary_key=True)
    rank_from = Column(Integer, nullable=False)
    rank_to = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class GrandArenaDefenceReward(Base):
    __tablename__ = 'grand_arena_defence_reward'

    id = Column(Integer, primary_key=True)
    limit_count = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class GrandArenaMaxRankReward(Base):
    __tablename__ = 'grand_arena_max_rank_reward'

    id = Column(Integer, primary_key=True)
    rank_from = Column(Integer, nullable=False)
    rank_to = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class GrandArenaMaxSeasonRankReward(Base):
    __tablename__ = 'grand_arena_max_season_rank_reward'

    id = Column(Integer, primary_key=True)
    rank_from = Column(Integer, nullable=False)
    rank_to = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class Guild(Base):
    __tablename__ = 'guild'

    guild_id = Column(Integer, primary_key=True)
    guild_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    guild_master = Column(Integer, nullable=False)
    member1 = Column(Integer, nullable=False)
    member2 = Column(Integer, nullable=False)
    member3 = Column(Integer, nullable=False)
    member4 = Column(Integer, nullable=False)
    member5 = Column(Integer, nullable=False)
    member6 = Column(Integer, nullable=False)
    member7 = Column(Integer, nullable=False)
    member8 = Column(Integer, nullable=False)
    member9 = Column(Integer, nullable=False)
    member10 = Column(Integer, nullable=False)
    member11 = Column(Integer, nullable=False)
    member12 = Column(Integer, nullable=False)
    member13 = Column(Integer, nullable=False)
    member14 = Column(Integer, nullable=False)
    member15 = Column(Integer, nullable=False)
    member16 = Column(Integer, nullable=False)
    member17 = Column(Integer, nullable=False)
    member18 = Column(Integer, nullable=False)
    member19 = Column(Integer, nullable=False)
    member20 = Column(Integer, nullable=False)
    member21 = Column(Integer, nullable=False)
    member22 = Column(Integer, nullable=False)
    member23 = Column(Integer, nullable=False)
    member24 = Column(Integer, nullable=False)
    member25 = Column(Integer, nullable=False)
    member26 = Column(Integer, nullable=False)
    member27 = Column(Integer, nullable=False)
    member28 = Column(Integer, nullable=False)
    member29 = Column(Integer, nullable=False)
    member30 = Column(Integer, nullable=False)


class HatsuneBgChange(Base):
    __tablename__ = 'hatsune_bg_change'

    area_id = Column(Integer, primary_key=True)
    quest_id_1 = Column(Integer, nullable=False)
    quest_id_2 = Column(Integer, nullable=False)
    quest_id_3 = Column(Integer, nullable=False)
    quest_id_4 = Column(Integer, nullable=False)
    quest_id_5 = Column(Integer, nullable=False)


class HatsuneBos(Base):
    __tablename__ = 'hatsune_boss'

    boss_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    area_id = Column(Integer, nullable=False)
    difficulty = Column(Integer, nullable=False)
    quest_name = Column(Text, nullable=False)
    position_x = Column(Integer, nullable=False)
    position_y = Column(Integer, nullable=False)
    boss_position_x = Column(Integer, nullable=False)
    boss_position_y = Column(Integer, nullable=False)
    result_boss_position_y = Column(Integer, nullable=False)
    icon_id = Column(Integer, nullable=False)
    use_ticket_num = Column(Integer, nullable=False)
    team_exp = Column(Integer, nullable=False)
    unit_exp = Column(Integer, nullable=False)
    love = Column(Integer, nullable=False)
    limit_time = Column(Integer, nullable=False)
    daily_limit = Column(Integer, nullable=False)
    clear_reward_group = Column(Integer, nullable=False)
    event_boss_treasure_box_id_1 = Column(Integer, nullable=False)
    background_1 = Column(Integer, nullable=False)
    wave_group_id_1 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_1 = Column(Text, nullable=False)
    wave_bgm_que_id_1 = Column(Text, nullable=False)
    story_id_wavestart_1 = Column(Integer, nullable=False)
    story_id_waveend_1 = Column(Integer, nullable=False)
    detail_bg_id = Column(Integer, nullable=False)
    detail_bg_position = Column(Integer, nullable=False)
    detail_boss_bg_size = Column(Float, nullable=False)
    detail_boss_bg_height = Column(Float, nullable=False)
    reward_gold_coefficient = Column(Text, nullable=False)
    reward_gold_limit = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    map_position_x = Column(Float, nullable=False)
    map_position_y = Column(Float, nullable=False)
    map_size = Column(Float, nullable=False)
    deatail_aura_size = Column(Float, nullable=False)
    map_aura_size = Column(Float, nullable=False)
    oneblow_count_of_skip_condition = Column(Integer, nullable=False)
    required_skip_ticket_count = Column(Integer, nullable=False)
    retire_flag = Column(Integer, nullable=False)
    disp_on_bg = Column(Integer, nullable=False)


class HatsuneBossCondition(Base):
    __tablename__ = 'hatsune_boss_condition'

    boss_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    condition_quest_id_1 = Column(Integer, nullable=False)
    condition_quest_id_2 = Column(Integer, nullable=False)
    condition_boss_id_1 = Column(Integer, nullable=False)
    condition_boss_id_2 = Column(Integer, nullable=False)
    condition_gacha_step = Column(Integer, nullable=False)
    force_unlock_time = Column(Text, nullable=False)
    release_quest_id_1 = Column(Integer, nullable=False)
    release_quest_id_2 = Column(Integer, nullable=False)
    release_boss_id_1 = Column(Integer, nullable=False)
    release_boss_id_2 = Column(Integer, nullable=False)


class HatsuneDailyMissionDatum(Base):
    __tablename__ = 'hatsune_daily_mission_data'

    daily_mission_id = Column(Integer, primary_key=True)
    disp_group = Column(Integer, nullable=False)
    category_icon = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    mission_condition = Column(Integer, nullable=False)
    condition_value_1 = Column(Integer)
    condition_value_2 = Column(Integer)
    condition_value_3 = Column(Integer)
    condition_num = Column(Integer, nullable=False)
    mission_reward_id = Column(Integer, nullable=False)
    system_id = Column(Integer)
    event_id = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class HatsuneDescription(Base):
    __tablename__ = 'hatsune_description'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    type = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)


class HatsuneEmblemMission(Base):
    __tablename__ = 'hatsune_emblem_mission'

    mission_id = Column(Integer, primary_key=True)
    disp_group = Column(Integer, nullable=False)
    category_icon = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    mission_condition = Column(Integer, nullable=False)
    condition_value_1 = Column(Integer, nullable=False)
    condition_value_2 = Column(Integer, nullable=False)
    condition_value_3 = Column(Integer, nullable=False)
    condition_num = Column(Integer, nullable=False)
    mission_reward_id = Column(Integer, nullable=False)
    system_id = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)
    visible_flag = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class HatsuneEmblemMissionReward(Base):
    __tablename__ = 'hatsune_emblem_mission_reward'

    id = Column(Integer, primary_key=True)
    mission_reward_id = Column(Integer, nullable=False, index=True)
    reward_type = Column(Integer, nullable=False)
    reward_id = Column(Integer, nullable=False, index=True)
    reward_num = Column(Integer, nullable=False)
    icon_type = Column(Integer, nullable=False)


class HatsuneItem(Base):
    __tablename__ = 'hatsune_item'

    event_id = Column(Integer, primary_key=True)
    boss_ticket_id = Column(Integer, nullable=False)
    gacha_ticket_id = Column(Integer, nullable=False)
    unit_material_id_1 = Column(Integer, nullable=False)
    unit_material_id_2 = Column(Integer, nullable=False)
    unit_material_id_3 = Column(Integer, nullable=False)
    unit_material_id_4 = Column(Integer, nullable=False)
    unit_material_id_5 = Column(Integer, nullable=False)
    unit_material_id_6 = Column(Integer, nullable=False)
    unit_material_id_7 = Column(Integer, nullable=False)
    unit_material_id_8 = Column(Integer, nullable=False)
    unit_material_id_9 = Column(Integer, nullable=False)
    unit_material_id_10 = Column(Integer, nullable=False)


class HatsuneMap(Base):
    __tablename__ = 'hatsune_map'

    course_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    name = Column(Text, nullable=False)
    map_id = Column(Integer, nullable=False)
    sheet_id = Column(Text, nullable=False)
    que_id = Column(Text, nullable=False)
    start_area_id = Column(Integer, nullable=False)
    end_area_id = Column(Integer, nullable=False)


class HatsuneMapEvent(Base):
    __tablename__ = 'hatsune_map_event'

    id = Column(Integer, primary_key=True)
    target_event_id = Column(Integer, nullable=False, index=True)
    event_type = Column(Integer, nullable=False)
    condition_id = Column(Integer, nullable=False)
    param1 = Column(Integer, nullable=False)
    param2 = Column(Integer, nullable=False)


class HatsuneMissionRewardDatum(Base):
    __tablename__ = 'hatsune_mission_reward_data'

    id = Column(Integer, primary_key=True)
    mission_reward_id = Column(Integer, nullable=False, index=True)
    reward_type = Column(Integer, nullable=False)
    reward_id = Column(Integer)
    reward_num = Column(Integer, nullable=False)


class HatsuneMultiRouteParameter(Base):
    __tablename__ = 'hatsune_multi_route_parameter'

    id = Column(Integer, primary_key=True)
    quest_id = Column(Integer, nullable=False, index=True)
    type = Column(Integer, nullable=False, index=True)
    param_1 = Column(Integer, nullable=False)
    param_2 = Column(Integer, nullable=False)
    param_3 = Column(Integer, nullable=False)
    text_1 = Column(Text, nullable=False)


class HatsunePresent(Base):
    __tablename__ = 'hatsune_present'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False, index=True)
    dialog_title = Column(Text, nullable=False)
    dialog_text = Column(Text, nullable=False)
    condition_quest_id = Column(Integer, nullable=False)
    condition_boss_id = Column(Integer, nullable=False)
    condition_mission_id = Column(Integer, nullable=False)
    adv_id = Column(Integer, nullable=False)
    item_type_1 = Column(Integer, nullable=False)
    item_id_1 = Column(Integer, nullable=False)
    item_num_1 = Column(Integer, nullable=False)
    item_type_2 = Column(Integer, nullable=False)
    item_id_2 = Column(Integer, nullable=False)
    item_num_2 = Column(Integer, nullable=False)
    item_type_3 = Column(Integer, nullable=False)
    item_id_3 = Column(Integer, nullable=False)
    item_num_3 = Column(Integer, nullable=False)
    item_type_4 = Column(Integer, nullable=False)
    item_id_4 = Column(Integer, nullable=False)
    item_num_4 = Column(Integer, nullable=False)
    item_type_5 = Column(Integer, nullable=False)
    item_id_5 = Column(Integer, nullable=False)
    item_num_5 = Column(Integer, nullable=False)


class HatsuneQuest(Base):
    __tablename__ = 'hatsune_quest'

    quest_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False, index=True)
    area_id = Column(Integer, nullable=False)
    quest_seq = Column(Integer, nullable=False)
    quest_name = Column(Text, nullable=False)
    position_x = Column(Integer, nullable=False)
    position_y = Column(Integer, nullable=False)
    icon_id = Column(Integer, nullable=False)
    stamina = Column(Integer, nullable=False)
    stamina_start = Column(Integer, nullable=False)
    team_exp = Column(Integer, nullable=False)
    unit_exp = Column(Integer, nullable=False)
    love = Column(Integer, nullable=False)
    limit_time = Column(Integer, nullable=False)
    daily_limit = Column(Integer, nullable=False)
    clear_reward_group = Column(Integer, nullable=False)
    rank_reward_group = Column(Integer, nullable=False)
    drop_reward_type = Column(Integer, nullable=False)
    drop_reward_id = Column(Integer, nullable=False)
    drop_reward_num = Column(Integer, nullable=False)
    drop_reward_odds = Column(Integer, nullable=False)
    background_1 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_1 = Column(Text, nullable=False)
    wave_bgm_que_id_1 = Column(Text, nullable=False)
    story_id_wavestart_1 = Column(Integer, nullable=False)
    story_id_waveend_1 = Column(Integer, nullable=False)
    background_2 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_2 = Column(Text, nullable=False)
    wave_bgm_que_id_2 = Column(Text, nullable=False)
    story_id_wavestart_2 = Column(Integer, nullable=False)
    story_id_waveend_2 = Column(Integer, nullable=False)
    background_3 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_3 = Column(Text, nullable=False)
    wave_bgm_que_id_3 = Column(Text, nullable=False)
    story_id_wavestart_3 = Column(Integer, nullable=False)
    story_id_waveend_3 = Column(Integer, nullable=False)
    quest_detail_bg_id = Column(Integer, nullable=False)
    quest_detail_bg_position = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class HatsuneQuestArea(Base):
    __tablename__ = 'hatsune_quest_area'

    area_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False, index=True)
    area_name = Column(Text, nullable=False)
    map_type = Column(Integer, nullable=False)
    sheet_id = Column(Text, nullable=False)
    que_id = Column(Text, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    area_disp = Column(Integer, nullable=False)
    map_id = Column(Integer, nullable=False)
    scroll_width = Column(Integer, nullable=False)
    scroll_height = Column(Integer, nullable=False)
    open_tutorial_id = Column(Integer, nullable=False)
    tutorial_param_1 = Column(Text, nullable=False)
    tutorial_param_2 = Column(Text, nullable=False)
    additional_effect = Column(Integer, nullable=False)


class HatsuneQuestCondition(Base):
    __tablename__ = 'hatsune_quest_condition'

    quest_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    condition_quest_id_1 = Column(Integer, nullable=False)
    condition_quest_id_2 = Column(Integer, nullable=False)
    condition_boss_id_1 = Column(Integer, nullable=False)
    condition_boss_id_2 = Column(Integer, nullable=False)
    release_quest_id_1 = Column(Integer, nullable=False)
    release_quest_id_2 = Column(Integer, nullable=False)
    release_boss_id_1 = Column(Integer, nullable=False)
    release_boss_id_2 = Column(Integer, nullable=False)
    condition_main_quest_id = Column(Integer, nullable=False)


class HatsuneQuiz(Base):
    __tablename__ = 'hatsune_quiz'

    event_id = Column(Integer, nullable=False, index=True)
    quiz_id = Column(Integer, primary_key=True)
    question_title = Column(Text, nullable=False)
    question = Column(Text, nullable=False)
    choice_1 = Column(Text, nullable=False)
    choice_2 = Column(Text, nullable=False)
    choice_3 = Column(Text, nullable=False)
    choice_4 = Column(Text, nullable=False)
    choice_5 = Column(Text, nullable=False)
    choice_6 = Column(Text, nullable=False)
    answer = Column(Integer, nullable=False)
    hint = Column(Text, nullable=False)
    resource_id = Column(Integer, nullable=False)
    release_quest_id = Column(Integer, nullable=False)
    quiz_position_x = Column(Integer, nullable=False)
    quiz_position_y = Column(Integer, nullable=False)
    quiz_icon_id = Column(Integer, nullable=False)
    quiz_point_name = Column(Text, nullable=False)
    adv_id_quiz_start = Column(Integer, nullable=False)
    adv_id_quiz_end = Column(Integer, nullable=False)


class HatsuneQuizCondition(Base):
    __tablename__ = 'hatsune_quiz_condition'
    __table_args__ = (
        Index('hatsune_quiz_condition_0_event_id_1_quiz_id', 'event_id', 'quiz_id'),
    )

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    quiz_id = Column(Integer, nullable=False)
    condition_quest_id = Column(Integer, nullable=False)
    condition_quiz_id = Column(Integer, nullable=False)
    condition_unit_id = Column(Integer, nullable=False)
    condition_mission_id = Column(Integer, nullable=False)
    condition_time_from = Column(Integer, nullable=False)


class HatsuneQuizReward(Base):
    __tablename__ = 'hatsune_quiz_reward'

    quiz_id = Column(Integer, primary_key=True)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class HatsuneSchedule(Base):
    __tablename__ = 'hatsune_schedule'

    event_id = Column(Integer, primary_key=True)
    teaser_time = Column(Text, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    close_time = Column(Text, nullable=False)
    background = Column(Integer, nullable=False)
    sheet_id = Column(Text, nullable=False)
    que_id = Column(Text, nullable=False)
    banner_unit_id = Column(Integer, nullable=False)
    count_start_time = Column(Text, nullable=False)
    backgroud_size_x = Column(Integer, nullable=False)
    backgroud_size_y = Column(Integer, nullable=False)
    backgroud_pos_x = Column(Integer, nullable=False)
    backgroud_pos_y = Column(Integer, nullable=False)
    original_event_id = Column(Integer, nullable=False)


class HatsuneSpecialBattle(Base):
    __tablename__ = 'hatsune_special_battle'

    event_id = Column(Integer, primary_key=True, nullable=False, index=True)
    mode = Column(Integer, primary_key=True, nullable=False)
    purpose_type = Column(Integer, nullable=False)
    purpose_count = Column(Integer, nullable=False)
    trigger_hp = Column(Integer, nullable=False)
    story_id_mode_start = Column(Integer, nullable=False)
    story_id_mode_end = Column(Integer, nullable=False)
    wave_group_id = Column(Integer, nullable=False)
    unnecessary_defeat_chara = Column(Integer, nullable=False)
    story_start_second = Column(Float, nullable=False)
    action_start_second = Column(Float, nullable=False)
    hp_gauge_color_flag = Column(Integer, nullable=False)
    start_idle_trigger = Column(Integer, nullable=False)
    appear_time = Column(Float, nullable=False)
    detail_boss_bg_size = Column(Float, nullable=False)
    detail_boss_bg_height = Column(Float, nullable=False)


class HatsuneSpecialBossTicketCount(Base):
    __tablename__ = 'hatsune_special_boss_ticket_count'

    id = Column(Integer, primary_key=True)
    challenge_count_from = Column(Integer, nullable=False)
    challenge_count_to = Column(Integer, nullable=False)
    use_ticket_num = Column(Integer, nullable=False)


class HatsuneSpecialEnemy(Base):
    __tablename__ = 'hatsune_special_enemy'

    enemy_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    mode = Column(Integer, nullable=False)
    enemy_point = Column(Integer, nullable=False)
    initial_position = Column(Integer, nullable=False)
    order = Column(Integer, nullable=False)


class HatsuneSpecialMissionDatum(Base):
    __tablename__ = 'hatsune_special_mission_data'

    special_mission_id = Column(Integer, primary_key=True)
    disp_group = Column(Integer, nullable=False)
    category_icon = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    mission_condition = Column(Integer, nullable=False)
    condition_value_1 = Column(Integer)
    condition_value_2 = Column(Integer)
    condition_value_3 = Column(Integer)
    condition_num = Column(Integer, nullable=False)
    mission_reward_id = Column(Integer, nullable=False)
    system_id = Column(Integer)
    event_id = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class HatsuneStationaryMissionDatum(Base):
    __tablename__ = 'hatsune_stationary_mission_data'

    stationary_mission_id = Column(Integer, primary_key=True)
    disp_group = Column(Integer, nullable=False)
    category_icon = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    mission_condition = Column(Integer, nullable=False)
    condition_value_1 = Column(Integer)
    condition_value_2 = Column(Integer)
    condition_value_3 = Column(Integer)
    condition_num = Column(Integer, nullable=False)
    mission_reward_id = Column(Integer, nullable=False)
    system_id = Column(Integer)
    event_id = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class HatsuneUnlockStoryCondition(Base):
    __tablename__ = 'hatsune_unlock_story_condition'

    story_id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    condition_entry = Column(Integer, nullable=False)
    condition_quest_id = Column(Integer, nullable=False)
    condition_boss_id = Column(Integer, nullable=False)
    condition_mission_id = Column(Integer, nullable=False)
    condition_time = Column(Text, nullable=False)


class HatsuneUnlockUnitCondition(Base):
    __tablename__ = 'hatsune_unlock_unit_condition'

    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)
    condition_mission_id = Column(Integer, nullable=False)
    top_description = Column(Text, nullable=False)
    description_1 = Column(Text, nullable=False)
    description_2 = Column(Text, nullable=False)


class ItemDatum(Base):
    __tablename__ = 'item_data'

    item_id = Column(Integer, primary_key=True)
    item_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    promotion_level = Column(Integer, nullable=False)
    item_type = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    limit_num = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class LoginBonusAdv(Base):
    __tablename__ = 'login_bonus_adv'

    id = Column(Integer, primary_key=True)
    login_bonus_id = Column(Integer, nullable=False, index=True)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    count_key = Column(Integer, nullable=False)
    adv_id = Column(Integer, nullable=False)


class LoginBonusDatum(Base):
    __tablename__ = 'login_bonus_data'

    login_bonus_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    login_bonus_type = Column(Integer, nullable=False)
    count_num = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    bg_id = Column(Integer, nullable=False)
    stamp_id = Column(Integer, nullable=False)
    odds_group_id = Column(Integer, nullable=False)
    adv_play_type = Column(Integer, nullable=False)
    count_type = Column(Integer, nullable=False)


class LoginBonusDetail(Base):
    __tablename__ = 'login_bonus_detail'
    __table_args__ = (
        Index('login_bonus_detail_0_login_bonus_id_1_count', 'login_bonus_id', 'count'),
    )

    id = Column(Integer, primary_key=True)
    login_bonus_id = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)
    reward_type = Column(Integer, nullable=False)
    reward_id = Column(Integer, nullable=False)
    reward_num = Column(Integer, nullable=False)
    character_id = Column(Integer, nullable=False)
    character_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    voice_id = Column(Integer, nullable=False)
    bg_id = Column(Integer, nullable=False)


class LoginBonusMessageDatum(Base):
    __tablename__ = 'login_bonus_message_data'

    id = Column(Integer, primary_key=True)
    login_bonus_id = Column(Integer, nullable=False, index=True)
    type = Column(Integer, nullable=False)
    day_count = Column(Integer, nullable=False)
    luck_pattern = Column(Integer, nullable=False)
    rate = Column(Integer, nullable=False)
    character_id = Column(Integer, nullable=False)
    character_name = Column(Text, nullable=False)
    message = Column(Text, nullable=False)
    voice_id = Column(Integer, nullable=False)


class LoveChara(Base):
    __tablename__ = 'love_chara'

    love_level = Column(Integer, primary_key=True)
    total_love = Column(Integer, nullable=False)
    unlocked_class = Column(Integer, nullable=False)
    rarity = Column(Integer, nullable=False)


class Minigame(Base):
    __tablename__ = 'minigame'

    id = Column(Integer, primary_key=True)
    minigame_scheme_id = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False, index=True)
    release_conditions_1 = Column(Integer, nullable=False)
    conditions_id_1 = Column(Integer, nullable=False)


class MissionRewardDatum(Base):
    __tablename__ = 'mission_reward_data'

    id = Column(Integer, primary_key=True)
    mission_reward_id = Column(Integer, nullable=False, index=True)
    reward_type = Column(Integer, nullable=False)
    reward_id = Column(Integer)
    reward_num = Column(Integer, nullable=False)


class Movie(Base):
    __tablename__ = 'movie'

    movie_id = Column(Integer, primary_key=True)
    story_group_id = Column(Integer, nullable=False)
    story_id = Column(Integer, nullable=False)
    bgm_id = Column(Text, nullable=False)
    se_id = Column(Text, nullable=False)


class MusicContent(Base):
    __tablename__ = 'music_content'

    music_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    total_playing_time = Column(Text, nullable=False)
    listen_start_time = Column(Text, nullable=False)
    detail = Column(Text, nullable=False)
    sheet_id = Column(Text, nullable=False)
    cue_id = Column(Text, nullable=False)


class MusicList(Base):
    __tablename__ = 'music_list'

    music_id = Column(Integer, primary_key=True)
    list_name = Column(Text, nullable=False)
    font_size = Column(Float, nullable=False)
    pre_shop_start = Column(Text, nullable=False)
    shop_start = Column(Text, nullable=False)
    shop_end = Column(Text, nullable=False)
    story_id = Column(Integer, nullable=False)
    cost_item_num = Column(Integer, nullable=False)
    sort = Column(Integer, nullable=False)
    kana = Column(Text, nullable=False)
    ios_url = Column(Text, nullable=False)
    android_url = Column(Text, nullable=False)
    dmm_url = Column(Text, nullable=False)


class NaviComment(Base):
    __tablename__ = 'navi_comment'

    comment_id = Column(Integer, primary_key=True)
    where_type = Column(Integer, nullable=False)
    character_id = Column(Integer, nullable=False)
    face_type = Column(Integer, nullable=False)
    character_name = Column(Text, nullable=False)
    description = Column(Text)
    voice_id = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    pos_x = Column(Float, nullable=False)
    pos_y = Column(Float, nullable=False)
    change_face_time = Column(Float, nullable=False)
    change_face_type = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)


class NotifDatum(Base):
    __tablename__ = 'notif_data'

    unit_id = Column(Integer, primary_key=True, nullable=False, index=True)
    notif_type = Column(Integer, primary_key=True, nullable=False)
    comment = Column(Text, nullable=False)


class OddsNameDatum(Base):
    __tablename__ = 'odds_name_data'

    id = Column(Integer, primary_key=True)
    odds_file = Column(Text, nullable=False)
    name = Column(Text, nullable=False)
    icon_type = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)


class PctComboCoefficient(Base):
    __tablename__ = 'pct_combo_coefficient'

    id = Column(Integer, primary_key=True)
    combo_min = Column(Integer, nullable=False)
    combo_max = Column(Integer, nullable=False)
    combo_coefficient = Column(Integer, nullable=False)


class PctEvaluation(Base):
    __tablename__ = 'pct_evaluation'

    evaluation_id = Column(Integer, primary_key=True)
    evaluation_point = Column(Integer, nullable=False)
    fever_point = Column(Integer, nullable=False)
    meet_width = Column(Integer, nullable=False)


class PctGamingMotion(Base):
    __tablename__ = 'pct_gaming_motion'

    motion_id = Column(Integer, primary_key=True)
    perfect_count = Column(Integer, nullable=False)
    good_count = Column(Integer, nullable=False)
    nice_count = Column(Integer, nullable=False)
    point = Column(Integer, nullable=False)


class PctItempoint(Base):
    __tablename__ = 'pct_itempoint'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, nullable=False, index=True)
    pct_point_coefficient = Column(Integer, nullable=False)


class PctResult(Base):
    __tablename__ = 'pct_result'

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, nullable=False, index=True)
    score_from = Column(Integer, nullable=False)
    score_to = Column(Integer, nullable=False)
    comment_id_1 = Column(Integer, nullable=False)
    comment_id_2 = Column(Integer, nullable=False)
    comment_id_3 = Column(Integer, nullable=False)
    comment_id_4 = Column(Integer, nullable=False)
    comment_id_5 = Column(Integer, nullable=False)


class PctReward(Base):
    __tablename__ = 'pct_reward'

    id = Column(Integer, primary_key=True)
    pct_point_type = Column(Integer, nullable=False, index=True)
    pct_point = Column(Integer, nullable=False)
    mission_detail = Column(Text, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_count_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_count_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_count_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_count_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_count_5 = Column(Integer, nullable=False)


class PctSystem(Base):
    __tablename__ = 'pct_system'

    id = Column(Integer, primary_key=True)
    pct_base_speed = Column(Integer, nullable=False)
    fever_point_max = Column(Integer, nullable=False)
    fever_time = Column(Integer, nullable=False)
    fever_revention_time = Column(Integer, nullable=False)
    pct_time = Column(Integer, nullable=False)
    chara1 = Column(Integer, nullable=False)
    chara2 = Column(Integer, nullable=False)
    chara1_gauge_choice = Column(Integer, nullable=False)
    chara2_gauge_choice = Column(Integer, nullable=False)


class PctSystemFruit(Base):
    __tablename__ = 'pct_system_fruits'

    id = Column(Integer, primary_key=True)
    last_time = Column(Integer, nullable=False)
    appearance = Column(Integer, nullable=False)
    bar_split = Column(Integer, nullable=False)
    appearance_chara_odds = Column(Integer, nullable=False)
    appearance_pattern = Column(Text, nullable=False)
    wait_time = Column(Integer, nullable=False)


class PctTapSpeed(Base):
    __tablename__ = 'pct_tap_speed'

    id = Column(Integer, primary_key=True)
    combo_count = Column(Integer, nullable=False)
    speed_magnification = Column(Integer, nullable=False)


class PositionSetting(Base):
    __tablename__ = 'position_setting'

    position_setting_id = Column(Integer, primary_key=True)
    front = Column(Integer, nullable=False)
    middle = Column(Integer, nullable=False)


class QuestAreaDatum(Base):
    __tablename__ = 'quest_area_data'

    area_id = Column(Integer, primary_key=True)
    area_name = Column(Text, nullable=False)
    map_type = Column(Integer, nullable=False)
    sheet_id = Column(Text, nullable=False)
    que_id = Column(Text, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class QuestConditionDatum(Base):
    __tablename__ = 'quest_condition_data'

    quest_id = Column(Integer, primary_key=True)
    condition_quest_id_1 = Column(Integer, nullable=False)
    condition_quest_id_2 = Column(Integer, nullable=False)
    condition_quest_id_3 = Column(Integer, nullable=False)
    condition_quest_id_4 = Column(Integer, nullable=False)
    condition_quest_id_5 = Column(Integer, nullable=False)
    release_quest_id_1 = Column(Integer, nullable=False)
    release_quest_id_2 = Column(Integer, nullable=False)
    release_quest_id_3 = Column(Integer, nullable=False)
    release_quest_id_4 = Column(Integer, nullable=False)
    release_quest_id_5 = Column(Integer, nullable=False)


class QuestDatum(Base):
    __tablename__ = 'quest_data'

    quest_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, nullable=False)
    quest_name = Column(Text, nullable=False)
    limit_team_level = Column(Integer, nullable=False)
    position_x = Column(Integer, nullable=False)
    position_y = Column(Integer, nullable=False)
    icon_id = Column(Integer, nullable=False)
    stamina = Column(Integer, nullable=False)
    stamina_start = Column(Integer, nullable=False)
    team_exp = Column(Integer, nullable=False)
    unit_exp = Column(Integer, nullable=False)
    love = Column(Integer, nullable=False)
    limit_time = Column(Integer, nullable=False)
    daily_limit = Column(Integer, nullable=False)
    clear_reward_group = Column(Integer, nullable=False)
    rank_reward_group = Column(Integer, nullable=False)
    background_1 = Column(Integer, nullable=False)
    wave_group_id_1 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_1 = Column(Text, nullable=False)
    wave_bgm_que_id_1 = Column(Text, nullable=False)
    story_id_wavestart_1 = Column(Integer, nullable=False)
    story_id_waveend_1 = Column(Integer, nullable=False)
    background_2 = Column(Integer, nullable=False)
    wave_group_id_2 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_2 = Column(Text, nullable=False)
    wave_bgm_que_id_2 = Column(Text, nullable=False)
    story_id_wavestart_2 = Column(Integer, nullable=False)
    story_id_waveend_2 = Column(Integer, nullable=False)
    background_3 = Column(Integer, nullable=False)
    wave_group_id_3 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_3 = Column(Text, nullable=False)
    wave_bgm_que_id_3 = Column(Text, nullable=False)
    story_id_wavestart_3 = Column(Integer, nullable=False)
    story_id_waveend_3 = Column(Integer, nullable=False)
    enemy_image_1 = Column(Integer, nullable=False)
    enemy_image_2 = Column(Integer, nullable=False)
    enemy_image_3 = Column(Integer, nullable=False)
    enemy_image_4 = Column(Integer, nullable=False)
    enemy_image_5 = Column(Integer, nullable=False)
    reward_image_1 = Column(Integer, nullable=False)
    reward_image_2 = Column(Integer, nullable=False)
    reward_image_3 = Column(Integer, nullable=False)
    reward_image_4 = Column(Integer, nullable=False)
    reward_image_5 = Column(Integer, nullable=False)
    quest_detail_bg_id = Column(Integer, nullable=False)
    quest_detail_bg_position = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class QuestDefeatNotice(Base):
    __tablename__ = 'quest_defeat_notice'

    id = Column(Integer, primary_key=True)
    image_id = Column(Integer, nullable=False)
    required_team_level = Column(Integer, nullable=False)
    required_quest_id = Column(Integer, nullable=False)


class QuestRewardDatum(Base):
    __tablename__ = 'quest_reward_data'

    reward_group_id = Column(Integer, primary_key=True)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class ResistDatum(Base):
    __tablename__ = 'resist_data'

    resist_status_id = Column(Integer, primary_key=True)
    ailment_1 = Column(Integer, nullable=False)
    ailment_2 = Column(Integer, nullable=False)
    ailment_3 = Column(Integer, nullable=False)
    ailment_4 = Column(Integer, nullable=False)
    ailment_5 = Column(Integer, nullable=False)
    ailment_6 = Column(Integer, nullable=False)
    ailment_7 = Column(Integer, nullable=False)
    ailment_8 = Column(Integer, nullable=False)
    ailment_9 = Column(Integer, nullable=False)
    ailment_10 = Column(Integer, nullable=False)
    ailment_11 = Column(Integer, nullable=False)
    ailment_12 = Column(Integer, nullable=False)
    ailment_13 = Column(Integer, nullable=False)
    ailment_14 = Column(Integer, nullable=False)
    ailment_15 = Column(Integer, nullable=False)
    ailment_16 = Column(Integer, nullable=False)
    ailment_17 = Column(Integer, nullable=False)
    ailment_18 = Column(Integer, nullable=False)
    ailment_19 = Column(Integer, nullable=False)
    ailment_20 = Column(Integer, nullable=False)


class RewardCollectGuide(Base):
    __tablename__ = 'reward_collect_guide'

    object_id = Column(Integer, primary_key=True)
    quest_id_1 = Column(Integer, nullable=False)
    quest_id_2 = Column(Integer, nullable=False)
    quest_id_3 = Column(Integer, nullable=False)
    quest_id_4 = Column(Integer, nullable=False)
    quest_id_5 = Column(Integer, nullable=False)
    quest_id_6 = Column(Integer, nullable=False)
    quest_id_7 = Column(Integer, nullable=False)
    quest_id_8 = Column(Integer, nullable=False)
    quest_id_9 = Column(Integer, nullable=False)
    quest_id_10 = Column(Integer, nullable=False)
    system_id_1 = Column(Integer, nullable=False)
    system_id_2 = Column(Integer, nullable=False)
    system_id_3 = Column(Integer, nullable=False)
    system_id_4 = Column(Integer, nullable=False)
    system_id_5 = Column(Integer, nullable=False)


class RoomChange(Base):
    __tablename__ = 'room_change'

    room_item_id = Column(Integer, primary_key=True)
    change_id = Column(Integer, nullable=False)
    change_start = Column(Text, nullable=False)
    change_end = Column(Text, nullable=False)


class RoomCharacterPersonality(Base):
    __tablename__ = 'room_character_personality'

    character_id = Column(Integer, primary_key=True)
    personality_id = Column(Integer, nullable=False)


class RoomChatFormation(Base):
    __tablename__ = 'room_chat_formation'

    id = Column(Integer, primary_key=True)
    unit_1_x = Column(Integer, nullable=False)
    unit_1_y = Column(Integer, nullable=False)
    unit_1_dir = Column(Integer, nullable=False)
    unit_2_x = Column(Integer, nullable=False)
    unit_2_y = Column(Integer, nullable=False)
    unit_2_dir = Column(Integer, nullable=False)
    unit_3_x = Column(Integer)
    unit_3_y = Column(Integer)
    unit_3_dir = Column(Integer)
    unit_4_x = Column(Integer)
    unit_4_y = Column(Integer)
    unit_4_dir = Column(Integer)
    unit_5_x = Column(Integer)
    unit_5_y = Column(Integer)
    unit_5_dir = Column(Integer)
    unit_num = Column(Integer, nullable=False)
    unit_id1 = Column(Integer)
    unit_id2 = Column(Integer)
    unit_id3 = Column(Integer)
    unit_id4 = Column(Integer)
    unit_id5 = Column(Integer)


class RoomChatInfo(Base):
    __tablename__ = 'room_chat_info'

    id = Column(Integer, primary_key=True)
    formation_id = Column(Integer, nullable=False)
    scenario_id = Column(Integer, nullable=False)


class RoomChatScenario(Base):
    __tablename__ = 'room_chat_scenario'

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    scenario_idx = Column(Integer, primary_key=True, nullable=False)
    unit_pos_no = Column(Integer, nullable=False)
    delay = Column(Integer, nullable=False)
    affect_type = Column(Integer, nullable=False)
    anime_id = Column(Integer, nullable=False)
    icon_id = Column(Integer, nullable=False)


class RoomEffect(Base):
    __tablename__ = 'room_effect'

    id = Column(Integer, primary_key=True)
    reward_get = Column(Integer, nullable=False)
    jukebox = Column(Integer, nullable=False)
    nebbia = Column(Integer, nullable=False)


class RoomEffectRewardGet(Base):
    __tablename__ = 'room_effect_reward_get'

    id = Column(Integer, primary_key=True, nullable=False)
    level = Column(Integer, primary_key=True, nullable=False)
    reward_type = Column(Integer, nullable=False)
    reward_id = Column(Integer, nullable=False)
    max_count = Column(Integer, nullable=False)
    inc_step = Column(Integer, nullable=False)
    interval_second = Column(Integer, nullable=False)


class RoomEmotionIcon(Base):
    __tablename__ = 'room_emotion_icon'

    id = Column(Integer, primary_key=True)
    enable_auto = Column(Integer, nullable=False)
    enable_tap = Column(Integer, nullable=False)


class RoomItem(Base):
    __tablename__ = 'room_item'

    id = Column(Integer, primary_key=True)
    item_type = Column(Integer, nullable=False)
    category = Column(Integer, nullable=False)
    name = Column(Text, nullable=False)
    max_level = Column(Integer, nullable=False)
    enable_remove = Column(Integer, nullable=False)
    max_possession_num = Column(Integer, nullable=False)
    effect_id_1 = Column(Integer, nullable=False)
    shop_start = Column(Text, nullable=False)
    shop_end = Column(Text, nullable=False)
    shop_new_disp_end = Column(Text, nullable=False)
    cost_item_num = Column(Integer, nullable=False)
    shop_open_type = Column(Integer, nullable=False)
    shop_open_id = Column(Integer, nullable=False)
    shop_open_value = Column(Integer, nullable=False)
    sold_price = Column(Integer, nullable=False)
    sort = Column(Integer, nullable=False)


class RoomItemAnnouncement(Base):
    __tablename__ = 'room_item_announcement'

    id = Column(Integer, primary_key=True)
    announcement_start = Column(Text, nullable=False)
    announcement_end = Column(Text, nullable=False)
    announcement_text = Column(Text, nullable=False)


class RoomItemDetail(Base):
    __tablename__ = 'room_item_detail'
    __table_args__ = (
        Index('room_item_detail_0_lvup_trigger_type_1_lvup_trigger_id', 'lvup_trigger_type', 'lvup_trigger_id'),
        Index('room_item_detail_0_lvup_trigger_type_2_1_lvup_trigger_id_2', 'lvup_trigger_type_2', 'lvup_trigger_id_2')
    )

    room_item_id = Column(Integer, primary_key=True, nullable=False)
    level = Column(Integer, primary_key=True, nullable=False)
    item_detail = Column(Text, nullable=False)
    lvup_trigger_type = Column(Integer, nullable=False)
    lvup_trigger_id = Column(Integer, nullable=False)
    lvup_trigger_value = Column(Integer, nullable=False)
    lvup_trigger_type_2 = Column(Integer, nullable=False)
    lvup_trigger_id_2 = Column(Integer, nullable=False)
    lvup_trigger_value_2 = Column(Integer, nullable=False)
    lvup_item1_type = Column(Integer, nullable=False)
    lvup_item1_id = Column(Integer, nullable=False)
    lvup_item1_num = Column(Integer, nullable=False)
    lvup_time = Column(Integer, nullable=False)


class RoomReleaseDatum(Base):
    __tablename__ = 'room_release_data'

    system_id = Column(Integer, primary_key=True)
    story_id = Column(Integer, nullable=False)
    pre_story_id = Column(Integer, nullable=False)


class RoomSetup(Base):
    __tablename__ = 'room_setup'

    room_item_id = Column(Integer, primary_key=True)
    grid_height = Column(Integer, nullable=False)
    grid_width = Column(Integer, nullable=False)
    unit_id = Column(Integer, nullable=False)


class RoomUnitComment(Base):
    __tablename__ = 'room_unit_comments'

    id = Column(Integer, nullable=False)
    unit_id = Column(Integer, primary_key=True, nullable=False, index=True)
    trigger = Column(Integer, primary_key=True, nullable=False)
    voice_id = Column(Integer, primary_key=True, nullable=False)
    beloved_step = Column(Integer, nullable=False)
    time = Column(Integer, primary_key=True, nullable=False)
    face_id = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    insert_word_type = Column(Integer, nullable=False)


class SeasonPack(Base):
    __tablename__ = 'season_pack'

    id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, nullable=False, index=True)
    disp_order = Column(Integer, nullable=False)
    category_icon = Column(Integer, nullable=False)
    receive_text = Column(Text, nullable=False)
    after_text = Column(Text, nullable=False)
    term = Column(Integer, nullable=False)
    repurchase_day = Column(Integer, nullable=False)
    group_id = Column(Integer, nullable=False)
    system_id_1 = Column(Integer, nullable=False)
    add_num_1 = Column(Integer, nullable=False)
    item_record_id = Column(Integer, nullable=False)
    condition_flg = Column(Integer, nullable=False)
    reward_rate_1 = Column(Integer, nullable=False)


class SekaiAddTimesDatum(Base):
    __tablename__ = 'sekai_add_times_data'

    id = Column(Integer, primary_key=True)
    sekai_id = Column(Integer, nullable=False)
    add_times = Column(Integer, nullable=False)
    add_times_limit = Column(Integer, nullable=False)
    add_times_time = Column(Text, nullable=False)
    duration = Column(Integer, nullable=False)


class SekaiBossDamageRankReward(Base):
    __tablename__ = 'sekai_boss_damage_rank_reward'

    id = Column(Integer, primary_key=True)
    damage_rank_id = Column(Integer, nullable=False)
    ranking_from = Column(Integer, nullable=False)
    ranking_to = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)


class SekaiBossFixReward(Base):
    __tablename__ = 'sekai_boss_fix_reward'

    sekai_id = Column(Integer, nullable=False)
    fix_reward_group_id = Column(Integer, nullable=False)
    fix_reward_id = Column(Integer, primary_key=True)
    boss_total_damage = Column(Text, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)
    reward_type_6 = Column(Integer, nullable=False)
    reward_id_6 = Column(Integer, nullable=False)
    reward_num_6 = Column(Integer, nullable=False)
    reward_type_7 = Column(Integer, nullable=False)
    reward_id_7 = Column(Integer, nullable=False)
    reward_num_7 = Column(Integer, nullable=False)
    reward_type_8 = Column(Integer, nullable=False)
    reward_id_8 = Column(Integer, nullable=False)
    reward_num_8 = Column(Integer, nullable=False)
    reward_type_9 = Column(Integer, nullable=False)
    reward_id_9 = Column(Integer, nullable=False)
    reward_num_9 = Column(Integer, nullable=False)
    reward_type_10 = Column(Integer, nullable=False)
    reward_id_10 = Column(Integer, nullable=False)
    reward_num_10 = Column(Integer, nullable=False)


class SekaiBossMode(Base):
    __tablename__ = 'sekai_boss_mode'

    sekai_boss_mode_id = Column(Integer, primary_key=True)
    sekai_enemy_id = Column(Integer, nullable=False)
    sekai_enemy_level = Column(Text, nullable=False)
    quest_detail_bg_id = Column(Integer, nullable=False)
    quest_detail_bg_position = Column(Integer, nullable=False)
    quest_detail_monster_size = Column(Float, nullable=False)
    quest_detail_monster_height = Column(Integer, nullable=False)
    limit_time = Column(Integer, nullable=False)
    background = Column(Integer, nullable=False)
    sheet_id = Column(Text, nullable=False)
    que_id = Column(Text, nullable=False)
    result_boss_position_y = Column(Integer, nullable=False)
    reward_gold_coefficient = Column(Integer, nullable=False)
    limited_mana = Column(Integer, nullable=False)
    score_coefficient = Column(Integer, nullable=False)


class SekaiEnemyParameter(Base):
    __tablename__ = 'sekai_enemy_parameter'

    sekai_enemy_id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, nullable=False)
    name = Column(Text, nullable=False)
    level = Column(Integer, nullable=False)
    rarity = Column(Integer, nullable=False)
    promotion_level = Column(Integer, nullable=False)
    hp = Column(Text, nullable=False)
    atk = Column(Integer, nullable=False)
    magic_str = Column(Integer, nullable=False)
    _def = Column('def', Integer, nullable=False)
    magic_def = Column(Integer, nullable=False)
    physical_critical = Column(Integer, nullable=False)
    magic_critical = Column(Integer, nullable=False)
    wave_hp_recovery = Column(Integer, nullable=False)
    wave_energy_recovery = Column(Integer, nullable=False)
    dodge = Column(Integer, nullable=False)
    physical_penetrate = Column(Integer, nullable=False)
    magic_penetrate = Column(Integer, nullable=False)
    life_steal = Column(Integer, nullable=False)
    hp_recovery_rate = Column(Integer, nullable=False)
    energy_recovery_rate = Column(Integer, nullable=False)
    energy_reduce_rate = Column(Integer, nullable=False)
    union_burst_level = Column(Integer, nullable=False)
    main_skill_lv_1 = Column(Integer, nullable=False)
    main_skill_lv_2 = Column(Integer, nullable=False)
    main_skill_lv_3 = Column(Integer, nullable=False)
    main_skill_lv_4 = Column(Integer, nullable=False)
    main_skill_lv_5 = Column(Integer, nullable=False)
    main_skill_lv_6 = Column(Integer, nullable=False)
    main_skill_lv_7 = Column(Integer, nullable=False)
    main_skill_lv_8 = Column(Integer, nullable=False)
    main_skill_lv_9 = Column(Integer, nullable=False)
    main_skill_lv_10 = Column(Integer, nullable=False)
    ex_skill_lv_1 = Column(Integer, nullable=False)
    ex_skill_lv_2 = Column(Integer, nullable=False)
    ex_skill_lv_3 = Column(Integer, nullable=False)
    ex_skill_lv_4 = Column(Integer, nullable=False)
    ex_skill_lv_5 = Column(Integer, nullable=False)
    resist_status_id = Column(Integer, nullable=False)
    accuracy = Column(Integer, nullable=False)


class SekaiSchedule(Base):
    __tablename__ = 'sekai_schedule'

    sekai_id = Column(Integer, primary_key=True)
    last_sekai_id = Column(Integer, nullable=False)
    fix_reward_group_id = Column(Integer, nullable=False)
    damage_rank_id = Column(Integer, nullable=False)
    teaser_time = Column(Text, nullable=False)
    start_time = Column(Text, nullable=False)
    count_start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    end_losstime = Column(Text, nullable=False)
    result_end = Column(Text, nullable=False)


class SekaiTopDatum(Base):
    __tablename__ = 'sekai_top_data'

    id = Column(Integer, primary_key=True)
    sekai_id = Column(Integer, nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    top_bg = Column(Integer, nullable=False)
    position_x = Column(Integer, nullable=False)
    position_y = Column(Integer, nullable=False)
    scale_ratio = Column(Float, nullable=False)
    sheet_id = Column(Text, nullable=False)
    que_id = Column(Text, nullable=False)
    boss_mode = Column(Integer, nullable=False)
    sekai_boss_mode_id = Column(Integer, nullable=False)
    boss_hp_from = Column(Text, nullable=False)
    boss_hp_to = Column(Text, nullable=False)
    boss_time_from = Column(Text, nullable=False)
    boss_time_to = Column(Text, nullable=False)
    duration = Column(Integer, nullable=False)
    story_id = Column(Integer, nullable=False)


class SekaiTopStoryDatum(Base):
    __tablename__ = 'sekai_top_story_data'

    sekai_id = Column(Integer, nullable=False)
    story_id = Column(Integer, primary_key=True)
    boss_time_from = Column(Text, nullable=False)
    boss_time_to = Column(Text, nullable=False)


class SekaiUnlockStoryCondition(Base):
    __tablename__ = 'sekai_unlock_story_condition'

    story_id = Column(Integer, primary_key=True)
    sekai_id = Column(Integer, nullable=False)
    condition_entry = Column(Integer, nullable=False)
    condition_fix_reward_id = Column(Integer, nullable=False)
    condition_time = Column(Text, nullable=False)


class ShopStaticPriceGroup(Base):
    __tablename__ = 'shop_static_price_group'

    id = Column(Integer, primary_key=True)
    price_group_id = Column(Integer, nullable=False)
    buy_count_from = Column(Integer, nullable=False)
    buy_count_to = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)


class SkillAction(Base):
    __tablename__ = 'skill_action'

    action_id = Column(Integer, primary_key=True)
    class_id = Column(Integer, nullable=False)
    action_type = Column(Integer, nullable=False)
    action_detail_1 = Column(Integer, nullable=False)
    action_detail_2 = Column(Integer, nullable=False)
    action_detail_3 = Column(Integer, nullable=False)
    action_value_1 = Column(Float, nullable=False)
    action_value_2 = Column(Float, nullable=False)
    action_value_3 = Column(Float, nullable=False)
    action_value_4 = Column(Float, nullable=False)
    action_value_5 = Column(Float, nullable=False)
    action_value_6 = Column(Float, nullable=False)
    action_value_7 = Column(Float, nullable=False)
    target_assignment = Column(Integer, nullable=False)
    target_area = Column(Integer, nullable=False)
    target_range = Column(Integer, nullable=False)
    target_type = Column(Integer, nullable=False)
    target_number = Column(Integer, nullable=False)
    target_count = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    level_up_disp = Column(Text, nullable=False)


class SkillCost(Base):
    __tablename__ = 'skill_cost'

    target_level = Column(Integer, primary_key=True)
    cost = Column(Integer, nullable=False)


class SkillDatum(Base):
    __tablename__ = 'skill_data'

    skill_id = Column(Integer, primary_key=True)
    name = Column(Text)
    skill_type = Column(Integer, nullable=False)
    skill_area_width = Column(Integer, nullable=False)
    skill_cast_time = Column(Float, nullable=False)
    action_1 = Column(Integer, nullable=False)
    action_2 = Column(Integer, nullable=False)
    action_3 = Column(Integer, nullable=False)
    action_4 = Column(Integer, nullable=False)
    action_5 = Column(Integer, nullable=False)
    action_6 = Column(Integer, nullable=False)
    action_7 = Column(Integer, nullable=False)
    depend_action_1 = Column(Integer, nullable=False)
    depend_action_2 = Column(Integer, nullable=False)
    depend_action_3 = Column(Integer, nullable=False)
    depend_action_4 = Column(Integer, nullable=False)
    depend_action_5 = Column(Integer, nullable=False)
    depend_action_6 = Column(Integer, nullable=False)
    depend_action_7 = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    icon_type = Column(Integer, nullable=False)


class SkipBossDatum(Base):
    __tablename__ = 'skip_boss_data'

    boss_id = Column(Integer, primary_key=True)
    skip_motion_id = Column(Integer, nullable=False)
    skip_bg_id = Column(Integer, nullable=False)
    skip_position_x = Column(Integer, nullable=False)
    skip_position_y = Column(Integer, nullable=False)
    skip_scale_x = Column(Float, nullable=False)
    skip_scale_y = Column(Float, nullable=False)


class SkipMonsterDatum(Base):
    __tablename__ = 'skip_monster_data'

    quest_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, nullable=False)
    quest_name = Column(Text, nullable=False)
    wave_group_id_1 = Column(Integer, nullable=False)
    bg_skip_id = Column(Integer, nullable=False)


class Stamp(Base):
    __tablename__ = 'stamp'

    stamp_id = Column(Integer, primary_key=True)
    disp_order = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    start_date = Column(Text, nullable=False)
    end_date = Column(Text, nullable=False)


class StationaryMissionDatum(Base):
    __tablename__ = 'stationary_mission_data'

    stationary_mission_id = Column(Integer, primary_key=True)
    disp_group = Column(Integer, nullable=False)
    category_icon = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)
    mission_condition = Column(Integer, nullable=False)
    condition_value_1 = Column(Integer)
    condition_value_2 = Column(Integer)
    condition_value_3 = Column(Integer)
    condition_num = Column(Integer, nullable=False)
    mission_reward_id = Column(Integer, nullable=False)
    system_id = Column(Integer)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class Still(Base):
    __tablename__ = 'still'

    still_id = Column(Integer, primary_key=True)
    story_group_id = Column(Integer, nullable=False)
    story_id = Column(Integer, nullable=False, index=True)
    still_group_id = Column(Integer, nullable=False)
    vertical_still_flg = Column(Integer, nullable=False)
    position_y = Column(Integer, nullable=False)
    unit_id_1 = Column(Integer, nullable=False)
    unit_id_2 = Column(Integer, nullable=False)
    unit_id_3 = Column(Integer, nullable=False)
    unit_id_4 = Column(Integer, nullable=False)
    unit_id_5 = Column(Integer, nullable=False)
    unit_id_6 = Column(Integer, nullable=False)
    unit_id_7 = Column(Integer, nullable=False)
    unit_id_8 = Column(Integer, nullable=False)
    unit_id_9 = Column(Integer, nullable=False)
    unit_id_10 = Column(Integer, nullable=False)
    facial_id = Column(Integer, nullable=False)
    album_ignore = Column(Integer, nullable=False)


class StoryCharacterMask(Base):
    __tablename__ = 'story_character_mask'

    chara_id = Column(Integer, primary_key=True)
    offset = Column(Float, nullable=False)
    size = Column(Float, nullable=False)
    softness = Column(Float, nullable=False)


class StoryDatum(Base):
    __tablename__ = 'story_data'

    story_group_id = Column(Integer, primary_key=True)
    story_type = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    thumbnail_id = Column(Integer, nullable=False)
    disp_order = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    order = Column(Integer, nullable=False)


class StoryDetail(Base):
    __tablename__ = 'story_detail'

    story_id = Column(Integer, primary_key=True)
    story_group_id = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    sub_title = Column(Text, nullable=False)
    visible_type = Column(Integer, nullable=False)
    story_end = Column(Integer, nullable=False)
    pre_story_id = Column(Integer, nullable=False)
    love_level = Column(Integer, nullable=False)
    requirement_id = Column(Integer, nullable=False)
    unlock_quest_id = Column(Integer, nullable=False)
    story_quest_id = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_value_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_value_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_value_3 = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class StoryQuestDatum(Base):
    __tablename__ = 'story_quest_data'

    story_quest_id = Column(Integer, primary_key=True)
    story_id = Column(Integer, nullable=False)
    quest_name = Column(Text, nullable=False)
    limit_time = Column(Integer, nullable=False)
    background_1 = Column(Integer, nullable=False)
    wave_group_id_1 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_1 = Column(Text, nullable=False)
    wave_bgm_que_id_1 = Column(Text, nullable=False)
    background_2 = Column(Integer, nullable=False)
    wave_group_id_2 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_2 = Column(Text, nullable=False)
    wave_bgm_que_id_2 = Column(Text, nullable=False)
    background_3 = Column(Integer, nullable=False)
    wave_group_id_3 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_3 = Column(Text, nullable=False)
    wave_bgm_que_id_3 = Column(Text, nullable=False)
    guest_unit_1 = Column(Integer, nullable=False)
    guest_unit_2 = Column(Integer, nullable=False)
    guest_unit_3 = Column(Integer, nullable=False)
    guest_unit_4 = Column(Integer, nullable=False)
    guest_unit_5 = Column(Integer, nullable=False)


class Tip(Base):
    __tablename__ = 'tips'

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    tips_index = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)


class TowerAreaDatum(Base):
    __tablename__ = 'tower_area_data'

    tower_area_id = Column(Integer, primary_key=True)
    max_floor_num = Column(Integer, nullable=False)
    area_bg = Column(Integer, nullable=False)
    tower_bgm = Column(Text, nullable=False)


class TowerEnemyParameter(Base):
    __tablename__ = 'tower_enemy_parameter'

    enemy_id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, nullable=False)
    name = Column(Text, nullable=False)
    level = Column(Integer, nullable=False)
    rarity = Column(Integer, nullable=False)
    promotion_level = Column(Integer, nullable=False)
    hp = Column(Integer, nullable=False)
    atk = Column(Integer, nullable=False)
    magic_str = Column(Integer, nullable=False)
    _def = Column('def', Integer, nullable=False)
    magic_def = Column(Integer, nullable=False)
    physical_critical = Column(Integer, nullable=False)
    magic_critical = Column(Integer, nullable=False)
    wave_hp_recovery = Column(Integer, nullable=False)
    wave_energy_recovery = Column(Integer, nullable=False)
    dodge = Column(Integer, nullable=False)
    physical_penetrate = Column(Integer, nullable=False)
    magic_penetrate = Column(Integer, nullable=False)
    life_steal = Column(Integer, nullable=False)
    hp_recovery_rate = Column(Integer, nullable=False)
    energy_recovery_rate = Column(Integer, nullable=False)
    energy_reduce_rate = Column(Integer, nullable=False)
    union_burst_level = Column(Integer, nullable=False)
    main_skill_lv_1 = Column(Integer, nullable=False)
    main_skill_lv_2 = Column(Integer, nullable=False)
    main_skill_lv_3 = Column(Integer, nullable=False)
    main_skill_lv_4 = Column(Integer, nullable=False)
    main_skill_lv_5 = Column(Integer, nullable=False)
    main_skill_lv_6 = Column(Integer, nullable=False)
    main_skill_lv_7 = Column(Integer, nullable=False)
    main_skill_lv_8 = Column(Integer, nullable=False)
    main_skill_lv_9 = Column(Integer, nullable=False)
    main_skill_lv_10 = Column(Integer, nullable=False)
    ex_skill_lv_1 = Column(Integer, nullable=False)
    ex_skill_lv_2 = Column(Integer, nullable=False)
    ex_skill_lv_3 = Column(Integer, nullable=False)
    ex_skill_lv_4 = Column(Integer, nullable=False)
    ex_skill_lv_5 = Column(Integer, nullable=False)
    resist_status_id = Column(Integer, nullable=False)
    accuracy = Column(Integer, nullable=False)
    enemy_color = Column(Integer, nullable=False)


class TowerExQuestDatum(Base):
    __tablename__ = 'tower_ex_quest_data'

    tower_ex_quest_id = Column(Integer, primary_key=True)
    tower_area_id = Column(Integer, nullable=False)
    floor_num = Column(Integer, nullable=False, index=True)
    stamina = Column(Integer, nullable=False)
    stamina_start = Column(Integer, nullable=False)
    team_exp = Column(Integer, nullable=False)
    limit_time = Column(Integer, nullable=False)
    reward_image_1 = Column(Integer, nullable=False)
    reward_count_1 = Column(Integer, nullable=False)
    reward_image_2 = Column(Integer, nullable=False)
    reward_count_2 = Column(Integer, nullable=False)
    reward_image_3 = Column(Integer, nullable=False)
    reward_count_3 = Column(Integer, nullable=False)
    reward_image_4 = Column(Integer, nullable=False)
    reward_count_4 = Column(Integer, nullable=False)
    reward_image_5 = Column(Integer, nullable=False)
    reward_count_5 = Column(Integer, nullable=False)
    additional_reward_type = Column(Integer, nullable=False)
    additional_reward_id = Column(Integer, nullable=False)
    fix_reward_group_id = Column(Integer, nullable=False)
    chest_id = Column(Integer, nullable=False)
    background = Column(Integer, nullable=False)
    bg_position = Column(Integer, nullable=False)
    wave_group_id = Column(Integer, nullable=False)
    enemy_position_x_1 = Column(Integer, nullable=False)
    enemy_local_position_y_1 = Column(Integer, nullable=False)
    enemy_size_1 = Column(Float, nullable=False)
    enemy_position_x_2 = Column(Integer, nullable=False)
    enemy_local_position_y_2 = Column(Integer, nullable=False)
    enemy_size_2 = Column(Float, nullable=False)
    enemy_position_x_3 = Column(Integer, nullable=False)
    enemy_local_position_y_3 = Column(Integer, nullable=False)
    enemy_size_3 = Column(Float, nullable=False)
    enemy_position_x_4 = Column(Integer, nullable=False)
    enemy_local_position_y_4 = Column(Integer, nullable=False)
    enemy_size_4 = Column(Float, nullable=False)
    enemy_position_x_5 = Column(Integer, nullable=False)
    enemy_local_position_y_5 = Column(Integer, nullable=False)
    enemy_size_5 = Column(Float, nullable=False)
    wave_bgm = Column(Text, nullable=False)
    clp_flag = Column(Integer, nullable=False)


class TowerQuestDatum(Base):
    __tablename__ = 'tower_quest_data'

    tower_quest_id = Column(Integer, primary_key=True)
    tower_area_id = Column(Integer, nullable=False)
    floor_num = Column(Integer, nullable=False, index=True)
    floor_image_type = Column(Integer, nullable=False)
    floor_image_add_type = Column(Integer, nullable=False)
    open_tower_ex_quest_id = Column(Integer, nullable=False)
    boss_floor_flg = Column(Integer, nullable=False)
    stamina = Column(Integer, nullable=False)
    stamina_start = Column(Integer, nullable=False)
    team_exp = Column(Integer, nullable=False)
    limit_time = Column(Integer, nullable=False)
    recovery_hp_rate = Column(Integer, nullable=False)
    recovery_tp_rate = Column(Integer, nullable=False)
    start_tp_rate = Column(Integer, nullable=False)
    reward_image_1 = Column(Integer, nullable=False)
    reward_count_1 = Column(Integer, nullable=False)
    reward_image_2 = Column(Integer, nullable=False)
    reward_count_2 = Column(Integer, nullable=False)
    reward_image_3 = Column(Integer, nullable=False)
    reward_count_3 = Column(Integer, nullable=False)
    reward_image_4 = Column(Integer, nullable=False)
    reward_count_4 = Column(Integer, nullable=False)
    reward_image_5 = Column(Integer, nullable=False)
    reward_count_5 = Column(Integer, nullable=False)
    additional_reward_type = Column(Integer, nullable=False)
    additional_reward_id = Column(Integer, nullable=False)
    fix_reward_group_id = Column(Integer, nullable=False)
    odds_group_id = Column(Integer, nullable=False)
    chest_id = Column(Integer, nullable=False)
    background = Column(Integer, nullable=False)
    bg_position = Column(Integer, nullable=False)
    wave_group_id = Column(Integer, nullable=False)
    enemy_position_x_1 = Column(Integer, nullable=False)
    enemy_local_position_y_1 = Column(Integer, nullable=False)
    enemy_size_1 = Column(Float, nullable=False)
    enemy_position_x_2 = Column(Integer, nullable=False)
    enemy_local_position_y_2 = Column(Integer, nullable=False)
    enemy_size_2 = Column(Float, nullable=False)
    enemy_position_x_3 = Column(Integer, nullable=False)
    enemy_local_position_y_3 = Column(Integer, nullable=False)
    enemy_size_3 = Column(Float, nullable=False)
    enemy_position_x_4 = Column(Integer, nullable=False)
    enemy_local_position_y_4 = Column(Integer, nullable=False)
    enemy_size_4 = Column(Float, nullable=False)
    enemy_position_x_5 = Column(Integer, nullable=False)
    enemy_local_position_y_5 = Column(Integer, nullable=False)
    enemy_size_5 = Column(Float, nullable=False)
    wave_bgm = Column(Text, nullable=False)
    clp_flag = Column(Integer, nullable=False)


class TowerQuestFixRewardGroup(Base):
    __tablename__ = 'tower_quest_fix_reward_group'

    fix_reward_group_id = Column(Integer, primary_key=True)
    treasure_type_1 = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_num_1 = Column(Integer, nullable=False)
    treasure_type_2 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_num_2 = Column(Integer, nullable=False)
    treasure_type_3 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_num_3 = Column(Integer, nullable=False)
    treasure_type_4 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    reward_id_4 = Column(Integer, nullable=False)
    reward_num_4 = Column(Integer, nullable=False)
    treasure_type_5 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    reward_id_5 = Column(Integer, nullable=False)
    reward_num_5 = Column(Integer, nullable=False)
    treasure_type_6 = Column(Integer, nullable=False)
    reward_type_6 = Column(Integer, nullable=False)
    reward_id_6 = Column(Integer, nullable=False)
    reward_num_6 = Column(Integer, nullable=False)
    treasure_type_7 = Column(Integer, nullable=False)
    reward_type_7 = Column(Integer, nullable=False)
    reward_id_7 = Column(Integer, nullable=False)
    reward_num_7 = Column(Integer, nullable=False)
    treasure_type_8 = Column(Integer, nullable=False)
    reward_type_8 = Column(Integer, nullable=False)
    reward_id_8 = Column(Integer, nullable=False)
    reward_num_8 = Column(Integer, nullable=False)
    treasure_type_9 = Column(Integer, nullable=False)
    reward_type_9 = Column(Integer, nullable=False)
    reward_id_9 = Column(Integer, nullable=False)
    reward_num_9 = Column(Integer, nullable=False)
    treasure_type_10 = Column(Integer, nullable=False)
    reward_type_10 = Column(Integer, nullable=False)
    reward_id_10 = Column(Integer, nullable=False)
    reward_num_10 = Column(Integer, nullable=False)


class TowerQuestOddsGroup(Base):
    __tablename__ = 'tower_quest_odds_group'

    odds_group_id = Column(Integer, primary_key=True, nullable=False, index=True)
    team_level_from = Column(Integer, primary_key=True, nullable=False)
    team_level_to = Column(Integer, primary_key=True, nullable=False)
    treasure_type_1 = Column(Integer, nullable=False)
    odds_csv_1 = Column(Text, nullable=False)
    treasure_type_2 = Column(Integer, nullable=False)
    odds_csv_2 = Column(Text, nullable=False)
    treasure_type_3 = Column(Integer, nullable=False)
    odds_csv_3 = Column(Text, nullable=False)
    treasure_type_4 = Column(Integer, nullable=False)
    odds_csv_4 = Column(Text, nullable=False)
    treasure_type_5 = Column(Integer, nullable=False)
    odds_csv_5 = Column(Text, nullable=False)
    treasure_type_6 = Column(Integer, nullable=False)
    odds_csv_6 = Column(Text, nullable=False)
    treasure_type_7 = Column(Integer, nullable=False)
    odds_csv_7 = Column(Text, nullable=False)
    treasure_type_8 = Column(Integer, nullable=False)
    odds_csv_8 = Column(Text, nullable=False)
    treasure_type_9 = Column(Integer, nullable=False)
    odds_csv_9 = Column(Text, nullable=False)
    treasure_type_10 = Column(Integer, nullable=False)
    odds_csv_10 = Column(Text, nullable=False)


class TowerSchedule(Base):
    __tablename__ = 'tower_schedule'

    tower_schedule_id = Column(Integer, primary_key=True)
    max_tower_area_id = Column(Integer, nullable=False)
    opening_story_id = Column(Integer, nullable=False, index=True)
    count_start_time = Column(Text, nullable=False)
    recovery_disable_time = Column(Text, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class TowerStoryDatum(Base):
    __tablename__ = 'tower_story_data'

    story_group_id = Column(Integer, primary_key=True)
    story_type = Column(Integer, nullable=False)
    value = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    thumbnail_id = Column(Integer, nullable=False)
    disp_order = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class TowerStoryDetail(Base):
    __tablename__ = 'tower_story_detail'

    story_id = Column(Integer, primary_key=True)
    story_group_id = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    sub_title = Column(Text, nullable=False)
    visible_type = Column(Integer, nullable=False)
    story_end = Column(Integer, nullable=False)
    pre_story_id = Column(Integer, nullable=False)
    love_level = Column(Integer, nullable=False)
    requirement_id = Column(Integer, nullable=False)
    unlock_quest_id = Column(Integer, nullable=False)
    story_quest_id = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    reward_id_1 = Column(Integer, nullable=False)
    reward_value_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    reward_id_2 = Column(Integer, nullable=False)
    reward_value_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    reward_id_3 = Column(Integer, nullable=False)
    reward_value_3 = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class TowerWaveGroupDatum(Base):
    __tablename__ = 'tower_wave_group_data'

    id = Column(Integer, nullable=False)
    wave_group_id = Column(Integer, primary_key=True)
    odds = Column(Integer, nullable=False)
    enemy_id_1 = Column(Integer, nullable=False)
    enemy_id_2 = Column(Integer, nullable=False)
    enemy_id_3 = Column(Integer, nullable=False)
    enemy_id_4 = Column(Integer, nullable=False)
    enemy_id_5 = Column(Integer, nullable=False)


class TrainingQuestDatum(Base):
    __tablename__ = 'training_quest_data'

    quest_id = Column(Integer, primary_key=True)
    area_id = Column(Integer, nullable=False)
    quest_name = Column(Text, nullable=False)
    limit_team_level = Column(Integer, nullable=False)
    unlock_quest_id_1 = Column(Integer, nullable=False)
    unlock_quest_id_2 = Column(Integer, nullable=False)
    stamina = Column(Integer, nullable=False)
    stamina_start = Column(Integer, nullable=False)
    team_exp = Column(Integer, nullable=False)
    unit_exp = Column(Integer, nullable=False)
    limit_time = Column(Integer, nullable=False)
    rank_reward_group = Column(Integer, nullable=False)
    background_1 = Column(Integer, nullable=False)
    wave_group_id_1 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_1 = Column(Text, nullable=False)
    wave_bgm_que_id_1 = Column(Text, nullable=False)
    background_2 = Column(Integer, nullable=False)
    wave_group_id_2 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_2 = Column(Text, nullable=False)
    wave_bgm_que_id_2 = Column(Text, nullable=False)
    background_3 = Column(Integer, nullable=False)
    wave_group_id_3 = Column(Integer, nullable=False)
    wave_bgm_sheet_id_3 = Column(Text, nullable=False)
    wave_bgm_que_id_3 = Column(Text, nullable=False)
    enemy_image_1 = Column(Integer, nullable=False)
    enemy_image_2 = Column(Integer, nullable=False)
    enemy_image_3 = Column(Integer, nullable=False)
    enemy_image_4 = Column(Integer, nullable=False)
    enemy_image_5 = Column(Integer, nullable=False)
    reward_image_1 = Column(Integer, nullable=False)
    reward_image_2 = Column(Integer, nullable=False)
    reward_image_3 = Column(Integer, nullable=False)
    reward_image_4 = Column(Integer, nullable=False)
    reward_image_5 = Column(Integer, nullable=False)
    training_quest_detail_bg_id = Column(Integer, nullable=False)
    training_quest_detail_bg_position = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class UniqueEquipmentCraft(Base):
    __tablename__ = 'unique_equipment_craft'

    equip_id = Column(Integer, primary_key=True)
    crafted_cost = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    item_id_1 = Column(Integer, nullable=False)
    consume_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    item_id_2 = Column(Integer, nullable=False)
    consume_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    item_id_3 = Column(Integer, nullable=False)
    consume_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    item_id_4 = Column(Integer, nullable=False)
    consume_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    item_id_5 = Column(Integer, nullable=False)
    consume_num_5 = Column(Integer, nullable=False)
    reward_type_6 = Column(Integer, nullable=False)
    item_id_6 = Column(Integer, nullable=False)
    consume_num_6 = Column(Integer, nullable=False)
    reward_type_7 = Column(Integer, nullable=False)
    item_id_7 = Column(Integer, nullable=False)
    consume_num_7 = Column(Integer, nullable=False)
    reward_type_8 = Column(Integer, nullable=False)
    item_id_8 = Column(Integer, nullable=False)
    consume_num_8 = Column(Integer, nullable=False)
    reward_type_9 = Column(Integer, nullable=False)
    item_id_9 = Column(Integer, nullable=False)
    consume_num_9 = Column(Integer, nullable=False)
    reward_type_10 = Column(Integer, nullable=False)
    item_id_10 = Column(Integer, nullable=False)
    consume_num_10 = Column(Integer, nullable=False)


class UniqueEquipmentDatum(Base):
    __tablename__ = 'unique_equipment_data'

    equipment_id = Column(Integer, primary_key=True)
    equipment_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    promotion_level = Column(Integer, nullable=False)
    craft_flg = Column(Integer, nullable=False)
    equipment_enhance_point = Column(Integer, nullable=False)
    sale_price = Column(Integer, nullable=False)
    require_level = Column(Integer, nullable=False)
    hp = Column(Float, nullable=False)
    atk = Column(Float, nullable=False)
    magic_str = Column(Float, nullable=False)
    _def = Column('def', Float, nullable=False)
    magic_def = Column(Float, nullable=False)
    physical_critical = Column(Float, nullable=False)
    magic_critical = Column(Float, nullable=False)
    wave_hp_recovery = Column(Float, nullable=False)
    wave_energy_recovery = Column(Float, nullable=False)
    dodge = Column(Float, nullable=False)
    physical_penetrate = Column(Float, nullable=False)
    magic_penetrate = Column(Float, nullable=False)
    life_steal = Column(Float, nullable=False)
    hp_recovery_rate = Column(Float, nullable=False)
    energy_recovery_rate = Column(Float, nullable=False)
    energy_reduce_rate = Column(Float, nullable=False)
    enable_donation = Column(Integer, nullable=False)
    accuracy = Column(Float, nullable=False)


class UniqueEquipmentEnhanceDatum(Base):
    __tablename__ = 'unique_equipment_enhance_data'

    equip_slot = Column(Integer, primary_key=True, nullable=False)
    enhance_level = Column(Integer, primary_key=True, nullable=False)
    needed_point = Column(Integer, nullable=False)
    total_point = Column(Integer, nullable=False)
    needed_mana = Column(Integer, nullable=False)
    rank = Column(Integer, nullable=False)


class UniqueEquipmentEnhanceRate(Base):
    __tablename__ = 'unique_equipment_enhance_rate'

    equipment_id = Column(Integer, primary_key=True)
    equipment_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    promotion_level = Column(Integer, nullable=False)
    hp = Column(Float, nullable=False)
    atk = Column(Float, nullable=False)
    magic_str = Column(Float, nullable=False)
    _def = Column('def', Float, nullable=False)
    magic_def = Column(Float, nullable=False)
    physical_critical = Column(Float, nullable=False)
    magic_critical = Column(Float, nullable=False)
    wave_hp_recovery = Column(Float, nullable=False)
    wave_energy_recovery = Column(Float, nullable=False)
    dodge = Column(Float, nullable=False)
    physical_penetrate = Column(Float, nullable=False)
    magic_penetrate = Column(Float, nullable=False)
    life_steal = Column(Float, nullable=False)
    hp_recovery_rate = Column(Float, nullable=False)
    energy_recovery_rate = Column(Float, nullable=False)
    energy_reduce_rate = Column(Float, nullable=False)
    accuracy = Column(Float, nullable=False)


class UniqueEquipmentRankup(Base):
    __tablename__ = 'unique_equipment_rankup'

    equip_id = Column(Integer, primary_key=True, nullable=False, index=True)
    unique_equip_rank = Column(Integer, primary_key=True, nullable=False)
    unit_level = Column(Integer, nullable=False)
    crafted_cost = Column(Integer, nullable=False)
    reward_type_1 = Column(Integer, nullable=False)
    item_id_1 = Column(Integer, nullable=False)
    consume_num_1 = Column(Integer, nullable=False)
    reward_type_2 = Column(Integer, nullable=False)
    item_id_2 = Column(Integer, nullable=False)
    consume_num_2 = Column(Integer, nullable=False)
    reward_type_3 = Column(Integer, nullable=False)
    item_id_3 = Column(Integer, nullable=False)
    consume_num_3 = Column(Integer, nullable=False)
    reward_type_4 = Column(Integer, nullable=False)
    item_id_4 = Column(Integer, nullable=False)
    consume_num_4 = Column(Integer, nullable=False)
    reward_type_5 = Column(Integer, nullable=False)
    item_id_5 = Column(Integer, nullable=False)
    consume_num_5 = Column(Integer, nullable=False)
    reward_type_6 = Column(Integer, nullable=False)
    item_id_6 = Column(Integer, nullable=False)
    consume_num_6 = Column(Integer, nullable=False)
    reward_type_7 = Column(Integer, nullable=False)
    item_id_7 = Column(Integer, nullable=False)
    consume_num_7 = Column(Integer, nullable=False)
    reward_type_8 = Column(Integer, nullable=False)
    item_id_8 = Column(Integer, nullable=False)
    consume_num_8 = Column(Integer, nullable=False)
    reward_type_9 = Column(Integer, nullable=False)
    item_id_9 = Column(Integer, nullable=False)
    consume_num_9 = Column(Integer, nullable=False)
    reward_type_10 = Column(Integer, nullable=False)
    item_id_10 = Column(Integer, nullable=False)
    consume_num_10 = Column(Integer, nullable=False)


class UnitAttackPattern(Base):
    __tablename__ = 'unit_attack_pattern'

    pattern_id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, nullable=False)
    loop_start = Column(Integer, nullable=False)
    loop_end = Column(Integer, nullable=False)
    atk_pattern_1 = Column(Integer, nullable=False)
    atk_pattern_2 = Column(Integer, nullable=False)
    atk_pattern_3 = Column(Integer, nullable=False)
    atk_pattern_4 = Column(Integer, nullable=False)
    atk_pattern_5 = Column(Integer, nullable=False)
    atk_pattern_6 = Column(Integer, nullable=False)
    atk_pattern_7 = Column(Integer, nullable=False)
    atk_pattern_8 = Column(Integer, nullable=False)
    atk_pattern_9 = Column(Integer, nullable=False)
    atk_pattern_10 = Column(Integer, nullable=False)
    atk_pattern_11 = Column(Integer, nullable=False)
    atk_pattern_12 = Column(Integer, nullable=False)
    atk_pattern_13 = Column(Integer, nullable=False)
    atk_pattern_14 = Column(Integer, nullable=False)
    atk_pattern_15 = Column(Integer, nullable=False)
    atk_pattern_16 = Column(Integer, nullable=False)
    atk_pattern_17 = Column(Integer, nullable=False)
    atk_pattern_18 = Column(Integer, nullable=False)
    atk_pattern_19 = Column(Integer, nullable=False)
    atk_pattern_20 = Column(Integer, nullable=False)


class UnitBackground(Base):
    __tablename__ = 'unit_background'

    unit_id = Column(Integer, primary_key=True)
    unit_name = Column(Text, nullable=False)
    bg_id = Column(Integer, nullable=False)
    bg_name = Column(Text, nullable=False)
    position = Column(Float, nullable=False)
    face_type = Column(Integer, nullable=False)


class UnitComment(Base):
    __tablename__ = 'unit_comments'
    __table_args__ = (
        Index('unit_comments_0_unit_id_1_use_type', 'unit_id', 'use_type'),
    )

    id = Column(Integer, primary_key=True)
    unit_id = Column(Integer, nullable=False, index=True)
    use_type = Column(Integer, nullable=False)
    voice_id = Column(Integer, nullable=False)
    face_id = Column(Integer, nullable=False)
    change_time = Column(Float, nullable=False)
    change_face = Column(Integer, nullable=False)
    description = Column(Text, nullable=False)


class UnitDatum(Base):
    __tablename__ = 'unit_data'

    unit_id = Column(Integer, primary_key=True)
    unit_name = Column(Text, nullable=False)
    kana = Column(Text, nullable=False)
    prefab_id = Column(Integer, nullable=False)
    rarity = Column(Integer, nullable=False)
    motion_type = Column(Integer, nullable=False)
    se_type = Column(Integer, nullable=False)
    move_speed = Column(Integer, nullable=False)
    search_area_width = Column(Integer, nullable=False)
    atk_type = Column(Integer, nullable=False)
    normal_atk_cast_time = Column(Float, nullable=False)
    cutin_1 = Column(Integer, nullable=False)
    cutin_2 = Column(Integer, nullable=False)
    guild_id = Column(Integer, nullable=False)
    exskill_display = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    only_disp_owned = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class UnitEnemyDatum(Base):
    __tablename__ = 'unit_enemy_data'

    unit_id = Column(Integer, primary_key=True)
    unit_name = Column(Text, nullable=False)
    prefab_id = Column(Integer, nullable=False)
    motion_type = Column(Integer, nullable=False)
    se_type = Column(Integer, nullable=False)
    move_speed = Column(Integer, nullable=False)
    search_area_width = Column(Integer, nullable=False)
    atk_type = Column(Integer, nullable=False)
    normal_atk_cast_time = Column(Float, nullable=False)
    cutin = Column(Integer, nullable=False)
    visual_change_flag = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)


class UnitIntroduction(Base):
    __tablename__ = 'unit_introduction'

    id = Column(Integer, primary_key=True)
    gacha_id = Column(Integer, nullable=False, index=True)
    introduction_number = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)
    maximum_chunk_size_1 = Column(Integer, nullable=False)
    maximum_chunk_size_loop_1 = Column(Integer, nullable=False)
    maximum_chunk_size_2 = Column(Integer, nullable=False)
    maximum_chunk_size_loop_2 = Column(Integer, nullable=False)
    maximum_chunk_size_3 = Column(Integer, nullable=False)
    maximum_chunk_size_loop_3 = Column(Integer, nullable=False)


class UnitMotionList(Base):
    __tablename__ = 'unit_motion_list'

    unit_id = Column(Integer, primary_key=True)
    sp_motion = Column(Integer, nullable=False)


class UnitMypagePo(Base):
    __tablename__ = 'unit_mypage_pos'

    id = Column(Integer, primary_key=True)
    pos_x = Column(Float, nullable=False)
    pos_y = Column(Float, nullable=False)
    scale = Column(Float, nullable=False)


class UnitProfile(Base):
    __tablename__ = 'unit_profile'

    unit_id = Column(Integer, primary_key=True)
    unit_name = Column(Text, nullable=False)
    age = Column(Text, nullable=False)
    guild = Column(Text, nullable=False)
    race = Column(Text, nullable=False)
    height = Column(Text, nullable=False)
    weight = Column(Text, nullable=False)
    birth_month = Column(Text, nullable=False)
    birth_day = Column(Text, nullable=False)
    blood_type = Column(Text, nullable=False)
    favorite = Column(Text, nullable=False)
    voice = Column(Text, nullable=False)
    voice_id = Column(Integer, nullable=False)
    catch_copy = Column(Text, nullable=False)
    self_text = Column(Text, nullable=False)
    guild_id = Column(Text, nullable=False)


class UnitPromotion(Base):
    __tablename__ = 'unit_promotion'

    unit_id = Column(Integer, primary_key=True, nullable=False, index=True)
    promotion_level = Column(Integer, primary_key=True, nullable=False)
    equip_slot_1 = Column(Integer, nullable=False)
    equip_slot_2 = Column(Integer, nullable=False)
    equip_slot_3 = Column(Integer, nullable=False)
    equip_slot_4 = Column(Integer, nullable=False)
    equip_slot_5 = Column(Integer, nullable=False)
    equip_slot_6 = Column(Integer, nullable=False)


class UnitPromotionStatu(Base):
    __tablename__ = 'unit_promotion_status'

    unit_id = Column(Integer, primary_key=True, nullable=False)
    promotion_level = Column(Integer, primary_key=True, nullable=False)
    hp = Column(Float, nullable=False)
    atk = Column(Float, nullable=False)
    magic_str = Column(Float, nullable=False)
    _def = Column('def', Float, nullable=False)
    magic_def = Column(Float, nullable=False)
    physical_critical = Column(Float, nullable=False)
    magic_critical = Column(Float, nullable=False)
    wave_hp_recovery = Column(Float, nullable=False)
    wave_energy_recovery = Column(Float, nullable=False)
    dodge = Column(Float, nullable=False)
    physical_penetrate = Column(Float, nullable=False)
    magic_penetrate = Column(Float, nullable=False)
    life_steal = Column(Float, nullable=False)
    hp_recovery_rate = Column(Float, nullable=False)
    energy_recovery_rate = Column(Float, nullable=False)
    energy_reduce_rate = Column(Float, nullable=False)
    accuracy = Column(Float, nullable=False)


class UnitRarity(Base):
    __tablename__ = 'unit_rarity'

    unit_id = Column(Integer, primary_key=True, nullable=False, index=True)
    rarity = Column(Integer, primary_key=True, nullable=False)
    hp = Column(Float, nullable=False)
    hp_growth = Column(Float, nullable=False)
    atk = Column(Float, nullable=False)
    atk_growth = Column(Float, nullable=False)
    magic_str = Column(Float, nullable=False)
    magic_str_growth = Column(Float, nullable=False)
    _def = Column('def', Float, nullable=False)
    def_growth = Column(Float, nullable=False)
    magic_def = Column(Float, nullable=False)
    magic_def_growth = Column(Float, nullable=False)
    physical_critical = Column(Float, nullable=False)
    physical_critical_growth = Column(Float, nullable=False)
    magic_critical = Column(Float, nullable=False)
    magic_critical_growth = Column(Float, nullable=False)
    wave_hp_recovery = Column(Float, nullable=False)
    wave_hp_recovery_growth = Column(Float, nullable=False)
    wave_energy_recovery = Column(Float, nullable=False)
    wave_energy_recovery_growth = Column(Float, nullable=False)
    dodge = Column(Float, nullable=False)
    dodge_growth = Column(Float, nullable=False)
    physical_penetrate = Column(Float, nullable=False)
    physical_penetrate_growth = Column(Float, nullable=False)
    magic_penetrate = Column(Float, nullable=False)
    magic_penetrate_growth = Column(Float, nullable=False)
    life_steal = Column(Float, nullable=False)
    life_steal_growth = Column(Float, nullable=False)
    hp_recovery_rate = Column(Float, nullable=False)
    hp_recovery_rate_growth = Column(Float, nullable=False)
    energy_recovery_rate = Column(Float, nullable=False)
    energy_recovery_rate_growth = Column(Float, nullable=False)
    energy_reduce_rate = Column(Float, nullable=False)
    energy_reduce_rate_growth = Column(Float, nullable=False)
    unit_material_id = Column(Integer, nullable=False, index=True)
    consume_num = Column(Integer, nullable=False)
    consume_gold = Column(Integer, nullable=False)
    accuracy = Column(Float, nullable=False)
    accuracy_growth = Column(Float, nullable=False)


class UnitSkillDatum(Base):
    __tablename__ = 'unit_skill_data'

    unit_id = Column(Integer, primary_key=True)
    union_burst = Column(Integer, nullable=False)
    main_skill_1 = Column(Integer, nullable=False)
    main_skill_2 = Column(Integer, nullable=False)
    main_skill_3 = Column(Integer, nullable=False)
    main_skill_4 = Column(Integer, nullable=False)
    main_skill_5 = Column(Integer, nullable=False)
    main_skill_6 = Column(Integer, nullable=False)
    main_skill_7 = Column(Integer, nullable=False)
    main_skill_8 = Column(Integer, nullable=False)
    main_skill_9 = Column(Integer, nullable=False)
    main_skill_10 = Column(Integer, nullable=False)
    ex_skill_1 = Column(Integer, nullable=False)
    ex_skill_evolution_1 = Column(Integer, nullable=False)
    ex_skill_2 = Column(Integer, nullable=False)
    ex_skill_evolution_2 = Column(Integer, nullable=False)
    ex_skill_3 = Column(Integer, nullable=False)
    ex_skill_evolution_3 = Column(Integer, nullable=False)
    ex_skill_4 = Column(Integer, nullable=False)
    ex_skill_evolution_4 = Column(Integer, nullable=False)
    ex_skill_5 = Column(Integer, nullable=False)
    ex_skill_evolution_5 = Column(Integer, nullable=False)
    sp_skill_1 = Column(Integer, nullable=False)
    sp_skill_2 = Column(Integer, nullable=False)
    sp_skill_3 = Column(Integer, nullable=False)
    sp_skill_4 = Column(Integer, nullable=False)
    sp_skill_5 = Column(Integer, nullable=False)
    union_burst_evolution = Column(Integer, nullable=False)
    main_skill_evolution_1 = Column(Integer, nullable=False)
    main_skill_evolution_2 = Column(Integer, nullable=False)


class UnitStatusCoefficient(Base):
    __tablename__ = 'unit_status_coefficient'

    coefficient_id = Column(Integer, primary_key=True)
    hp_coefficient = Column(Float, nullable=False)
    atk_coefficient = Column(Float, nullable=False)
    magic_str_coefficient = Column(Float, nullable=False)
    def_coefficient = Column(Float, nullable=False)
    magic_def_coefficient = Column(Float, nullable=False)
    physical_critical_coefficient = Column(Float, nullable=False)
    magic_critical_coefficient = Column(Float, nullable=False)
    wave_hp_recovery_coefficient = Column(Float, nullable=False)
    wave_energy_recovery_coefficient = Column(Float, nullable=False)
    dodge_coefficient = Column(Float, nullable=False)
    physical_penetrate_coefficient = Column(Float, nullable=False)
    magic_penetrate_coefficient = Column(Float, nullable=False)
    life_steal_coefficient = Column(Float, nullable=False)
    hp_recovery_rate_coefficient = Column(Float, nullable=False)
    energy_recovery_rate_coefficient = Column(Float, nullable=False)
    energy_reduce_rate_coefficient = Column(Float, nullable=False)
    skill_lv_coefficient = Column(Float, nullable=False)
    exskill_evolution_coefficient = Column(Integer, nullable=False)
    overall_coefficient = Column(Float, nullable=False)
    accuracy_coefficient = Column(Float, nullable=False)
    skill1_evolution_coefficient = Column(Integer, nullable=False)
    skill1_evolution_slv_coefficient = Column(Float, nullable=False)


class UnitUniqueEquip(Base):
    __tablename__ = 'unit_unique_equip'

    unit_id = Column(Integer, primary_key=True)
    equip_slot = Column(Integer, nullable=False)
    equip_id = Column(Integer, nullable=False)


class UnlockSkillDatum(Base):
    __tablename__ = 'unlock_skill_data'

    promotion_level = Column(Integer, nullable=False)
    unlock_skill = Column(Integer, primary_key=True)


class UnlockUnitCondition(Base):
    __tablename__ = 'unlock_unit_condition'

    unit_id = Column(Integer, primary_key=True)
    unit_name = Column(Text, nullable=False)
    class_id = Column(Integer, nullable=False)
    pre_unit_id = Column(Integer, nullable=False)
    condition_type_1 = Column(Integer, nullable=False)
    condition_type_detail_1 = Column(Integer, nullable=False)
    condition_id_1 = Column(Integer, nullable=False)
    count_1 = Column(Integer, nullable=False)
    condition_type_2 = Column(Integer, nullable=False)
    condition_type_detail_2 = Column(Integer, nullable=False)
    condition_id_2 = Column(Integer, nullable=False)
    count_2 = Column(Integer, nullable=False)
    condition_type_3 = Column(Integer, nullable=False)
    condition_type_detail_3 = Column(Integer, nullable=False)
    condition_id_3 = Column(Integer, nullable=False)
    count_3 = Column(Integer, nullable=False)
    condition_type_4 = Column(Integer, nullable=False)
    condition_type_detail_4 = Column(Integer, nullable=False)
    condition_id_4 = Column(Integer, nullable=False)
    count_4 = Column(Integer, nullable=False)
    condition_type_5 = Column(Integer, nullable=False)
    condition_type_detail_5 = Column(Integer, nullable=False)
    condition_id_5 = Column(Integer, nullable=False)
    count_5 = Column(Integer, nullable=False)
    release_effect_type = Column(Integer, nullable=False)


class VisualCustomize(Base):
    __tablename__ = 'visual_customize'

    id = Column(Integer, primary_key=True)
    title_prefab = Column(Integer, nullable=False)
    title_movie = Column(Integer, nullable=False)
    title_voice = Column(Integer, nullable=False)
    story_top_movie = Column(Integer, nullable=False)
    quest_top_movie = Column(Integer, nullable=False)
    start_time = Column(Text, nullable=False)
    end_time = Column(Text, nullable=False)


class VoiceGroup(Base):
    __tablename__ = 'voice_group'

    group_id = Column(Integer, primary_key=True)
    group_id_comment = Column(Text, nullable=False)
    group_unit_id_01 = Column(Integer, nullable=False)
    group_unit_id_02 = Column(Integer, nullable=False)
    group_unit_id_03 = Column(Integer, nullable=False)
    group_unit_id_04 = Column(Integer, nullable=False)
    group_unit_id_05 = Column(Integer, nullable=False)


class VoiceGroupChara(Base):
    __tablename__ = 'voice_group_chara'

    group_unit_id = Column(Integer, primary_key=True)
    group_unit_id_comment = Column(Text, nullable=False)
    unit_id_01 = Column(Integer, nullable=False)
    unit_id_02 = Column(Integer, nullable=False)
    unit_id_03 = Column(Integer, nullable=False)
    unit_id_04 = Column(Integer, nullable=False)
    unit_id_05 = Column(Integer, nullable=False)
    unit_id_06 = Column(Integer, nullable=False)
    unit_id_07 = Column(Integer, nullable=False)
    unit_id_08 = Column(Integer, nullable=False)
    unit_id_09 = Column(Integer, nullable=False)
    unit_id_10 = Column(Integer, nullable=False)


class VoteDatum(Base):
    __tablename__ = 'vote_data'

    vote_id = Column(Integer, primary_key=True)
    vote_start_time = Column(Text, nullable=False)
    vote_end_time = Column(Text, nullable=False)
    result_start_time = Column(Text, nullable=False)
    result_end_time = Column(Text, nullable=False)
    start_story_id = Column(Integer, nullable=False)
    result_story_id = Column(Integer, nullable=False)


class VoteInfo(Base):
    __tablename__ = 'vote_info'

    vote_id = Column(Integer, primary_key=True, nullable=False)
    vote_help_index = Column(Integer, primary_key=True, nullable=False)
    vote_title = Column(Text, nullable=False)
    vote_help = Column(Text, nullable=False)


class VoteUnit(Base):
    __tablename__ = 'vote_unit'

    vote_id = Column(Integer, primary_key=True, nullable=False)
    unit_id = Column(Integer, primary_key=True, nullable=False)
    unit_rarity = Column(Integer, nullable=False)


class WaveGroupDatum(Base):
    __tablename__ = 'wave_group_data'

    id = Column(Integer, primary_key=True)
    wave_group_id = Column(Integer, nullable=False)
    odds = Column(Integer, nullable=False)
    enemy_id_1 = Column(Integer, nullable=False)
    drop_gold_1 = Column(Integer, nullable=False)
    drop_reward_id_1 = Column(Integer, nullable=False)
    enemy_id_2 = Column(Integer, nullable=False)
    drop_gold_2 = Column(Integer, nullable=False)
    drop_reward_id_2 = Column(Integer, nullable=False)
    enemy_id_3 = Column(Integer, nullable=False)
    drop_gold_3 = Column(Integer, nullable=False)
    drop_reward_id_3 = Column(Integer, nullable=False)
    enemy_id_4 = Column(Integer, nullable=False)
    drop_gold_4 = Column(Integer, nullable=False)
    drop_reward_id_4 = Column(Integer, nullable=False)
    enemy_id_5 = Column(Integer, nullable=False)
    drop_gold_5 = Column(Integer, nullable=False)
    drop_reward_id_5 = Column(Integer, nullable=False)


class Worldmap(Base):
    __tablename__ = 'worldmap'

    course_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    map_id = Column(Integer, nullable=False)
    sheet_id = Column(Text, nullable=False)
    que_id = Column(Text, nullable=False)
    start_area_id = Column(Integer, nullable=False)
    end_area_id = Column(Integer, nullable=False)
