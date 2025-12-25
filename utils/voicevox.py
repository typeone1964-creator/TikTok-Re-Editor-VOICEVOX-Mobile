import requests
import json
from typing import List, Dict, Optional


class VoiceVoxAPI:
    def __init__(self, mode: str = "local", base_url: str = "http://localhost:50021", cloud_api_key: str = ""):
        """
        VOICEVOXのAPIクライアント

        Args:
            mode: "local" (ローカル版) or "cloud" (クラウド版)
            base_url: ローカル版のベースURL
            cloud_api_key: クラウド版のAPIキー
        """
        self.mode = mode
        self.base_url = base_url
        self.cloud_api_key = cloud_api_key
        self.cloud_endpoint = "https://deprecatedapis.tts.quest/v2/voicevox/audio/"
        self.cloud_speakers_endpoint = "https://deprecatedapis.tts.quest/v2/voicevox/speakers/"

    def get_speakers(self) -> List[Dict]:
        """VOICEVOXのスピーカー一覧を取得"""
        try:
            if self.mode == "cloud":
                # クラウド版の場合
                response = requests.get(
                    self.cloud_speakers_endpoint,
                    params={"key": self.cloud_api_key}
                )
            else:
                # ローカル版の場合
                response = requests.get(f"{self.base_url}/speakers")

            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"スピーカー取得エラー: {e}")
            return []

    def get_speaker_styles(self, speakers: List[Dict]) -> Dict[str, List[Dict]]:
        """スピーカーとスタイルの辞書を作成"""
        speaker_styles = {}
        for speaker in speakers:
            speaker_name = speaker.get("name", "")
            styles = speaker.get("styles", [])
            speaker_styles[speaker_name] = styles
        return speaker_styles

    def find_speaker_id(self, speakers: List[Dict], speaker_name: str, style_name: str = "ノーマル") -> Optional[int]:
        """指定されたスピーカー名とスタイル名からスピーカーIDを取得"""
        for speaker in speakers:
            if speaker.get("name") == speaker_name:
                for style in speaker.get("styles", []):
                    if style.get("name") == style_name:
                        return style.get("id")
        return None

    def generate_audio_query(self, text: str, speaker_id: int) -> Optional[Dict]:
        """テキストから音声クエリを生成"""
        try:
            response = requests.post(
                f"{self.base_url}/audio_query",
                params={"text": text, "speaker": speaker_id}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"音声クエリ生成エラー: {e}")
            return None

    def synthesize_voice(self, audio_query: Dict, speaker_id: int, speed: float = 1.2) -> Optional[bytes]:
        """音声クエリから音声を合成"""
        try:
            # 話速を設定
            audio_query["speedScale"] = speed

            response = requests.post(
                f"{self.base_url}/synthesis",
                params={"speaker": speaker_id},
                headers={"Content-Type": "application/json"},
                data=json.dumps(audio_query)
            )
            response.raise_for_status()
            return response.content
        except Exception as e:
            print(f"音声合成エラー: {e}")
            return None

    def generate_voice(self, text: str, speaker_id: int, speed: float = 1.0) -> Optional[bytes]:
        """テキストから直接音声を生成（便利メソッド）"""
        if self.mode == "cloud":
            # クラウド版：1ステップで音声生成
            return self.generate_voice_cloud(text, speaker_id, speed)
        else:
            # ローカル版：2ステップで音声生成
            audio_query = self.generate_audio_query(text, speaker_id)
            if audio_query:
                return self.synthesize_voice(audio_query, speaker_id, speed)
            return None

    def generate_voice_cloud(self, text: str, speaker_id: int, speed: float = 1.0) -> Optional[bytes]:
        """クラウドAPIを使用して音声を生成"""
        try:
            response = requests.post(
                self.cloud_endpoint,
                data={
                    "key": self.cloud_api_key,
                    "speaker": speaker_id,
                    "text": text,
                    "speed": speed
                }
            )
            response.raise_for_status()
            return response.content
        except Exception as e:
            print(f"クラウド音声生成エラー: {e}")
            return None

    def generate_sample_voice(self, speaker_id: int) -> Optional[bytes]:
        """キャラクター試聴用のサンプル音声を生成"""
        sample_text = "こんにちは、VOICEVOXです。よろしくお願いします。"
        return self.generate_voice(sample_text, speaker_id, speed=1.0)
